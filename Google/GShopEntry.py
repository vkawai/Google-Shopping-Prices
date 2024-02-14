class GShopEntry:
    
    store_name: str
    details: str
    price: float
    shipping_info: str
    store_url_link: str

    def __init__(self, store_name: str, details: str, price: float, shipping_info: str, store_url_link: str) -> None:
        self.store_name = store_name
        self.details = details
        self.price = price
        self.shipping_info = shipping_info
        self.store_url = store_url_link