import time
import json

import Helpers

from Google.GShop import GShop
from Google.GShopEntry import GShopEntry
from Notion.NDatabase import NDatabase
from Notion.NDatabaseProperty import NDatabaseProperty
from PropertyBuilder import PropertyBuilder

from notion_client import Client

class ProductEntry:
    variant: str
    url: str
    data: list[GShopEntry]

    def __init__(self, dict) -> None:
        self.variant = dict["variant"]
        self.url = dict["url"]
        self.data = {}

class PriceScrapper:

    database: NDatabase
    entries: list[ProductEntry]
    
    def __init__(self, json_config_file: str = 'config.json') -> None:
        # load notion config file
        file = open(json_config_file)
        data = json.load(file)
        client = Client(auth=data["api_key"])
        self.database = NDatabase(client=client, database_id=data["database_id"])
        self.entries = []
        for product_data in data["products"]:
            self.entries.append(ProductEntry(product_data))

    def process(self):
        self.load_gshop_data()
        self.add_data_to_notion()

    def load_gshop_data(self):
        """load data from google shopping"""
        print(f'Fetching data from google shopping')
        for entry in self.entries:
            entry.data = GShop.get_stores_prices(entry.url)

    def add_data_to_notion(self):
        print(f'Adding data from google shopping to Notion database')
        for entry in self.entries:
            for data in entry.data:
                self.process_entry(entry.variant, data)
                time.sleep(0.4) # Needed to avoid flooding Notion API

    def process_entry(self, product: str, entry: GShopEntry):
        db_entry = self.database.get_db_entry(entry)
        if not db_entry["results"]:
            print(f'Creating entry: {entry.store_name} ({entry.store_url})')
            self.database.add_entry(Helpers.gpu_properties(entry, product))
        else:
            print(f'Updating entry: {entry.store_name} ({entry.store_url})')
            page_id = db_entry["results"][0]["id"]
            price_property_id = db_entry["results"][0]["properties"]["Price"]["id"]
            self.database.update_entry(page_id, Helpers.update_price(price_property_id, entry.price))

    
print(f'Starting price scrapping')
price_scrapper = PriceScrapper()
price_scrapper.process()
print(f'Operationg ended')
