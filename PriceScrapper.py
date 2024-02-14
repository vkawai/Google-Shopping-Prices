
import time
import json

from Google.GShop import GShop
from Google.GShopEntry import GShopEntry
from Notion.NDatabase import NDatabase

from notion_client import Client

# load notion config file
file = open('config.json')
data = json.load(file)

api_key = data["api_key"]
database_id = data["database_id"]

blk_variant_url = data["variant_a_url"]
wht_variant_url = data["variant_b_url"]

# load data from google shopping
print(f'Fetching data from google shopping')
blk_data = GShop.get_stores_prices(blk_variant_url)
wht_data = GShop.get_stores_prices(wht_variant_url)

# setup notion client
print(f'Configuring notion client')
client = Client(auth=api_key)
database = NDatabase(client, client, database_id)

wait_time = 0.4 # Needed to avoid flooding Notion API

def process_entry(entry: GShopEntry, variant: str):
    db_entry = database.get_db_entry(entry)
    if not db_entry["results"]:
        print(f'Creating entry: {entry.store_name} ({entry.store_url})')
        database.add_product_entry(entry, variant)
    else:
        print(f'Updating entry: {entry.store_name} ({entry.store_url})')
        page_id = db_entry["results"][0]["id"]
        price_property_id = db_entry["results"][0]["properties"]["Price"]["id"]
        database.update_product_price(page_id, price_property_id, entry.price)

for entry in blk_data:
    process_entry(entry, "Black")
    time.sleep(wait_time)
    
for entry in wht_data:
    process_entry(entry, "White")
    time.sleep(wait_time)

print(f'Operationg ended.')