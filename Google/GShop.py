import requests

from Google.GShopEntry import GShopEntry
from parsel import Selector
from price_parser import Price

class GShop:
    def request_product_comparison_data(url: str) -> Selector:
        """
        Get stores prices from given URL.

        URL must be a product information url (the one that shows all stores selling it)
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }
        html = requests.get(url, headers=headers, timeout=30)
        return Selector(html.text)


    def parse_product_comparison_data(selector: Selector):
        """Parse result from request_product_comparison_data function"""
        google_shopping_data = []
        
        for result in selector.css(".sh-osd__offer-row"):
            product_name = selector.css(".BvQan::text").get()
            store_name = result.css(".b5ycib.shntl::text").get()
            details = result.css(".SH30Lb.yGibJf div::text").get()
            price_value = result.css(".drzWO::text").get()
            price = Price.fromstring(price_value).amount_float
            shipping_fee = result.css(".rt9Bpc::text").get()
            
            store_url_value = result.css(".UxuaJe::attr(href)").get()
            store_url_link = store_url_value.replace("/url?q=", '').split('%')[0]

            google_shopping_data.append(GShopEntry(product_name, store_name, details, price, shipping_fee, store_url_link))
            
        return google_shopping_data
    
    def get_stores_prices(url: str) -> list[GShopEntry]:
        """Gets data from url, and parses to a list of GShopEntry objects"""
        data = GShop.request_product_comparison_data(url)
        return GShop.parse_product_comparison_data(data)