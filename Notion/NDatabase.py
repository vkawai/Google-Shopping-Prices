from Notion.NDatabaseProperty import NDatabaseProperty
from Google.GShop import GShopEntry
from notion_client import Client

class NDatabase:
    def __init__(self, client: Client, auth_key: str, database_id: str) -> None:
        self.notion = client
        self.database_id = database_id

    def get_db_entry(self, entry: GShopEntry):
        return self.notion.databases.query(database_id="1ba2216875c8429ab7baebb27fa74f7f", **{
            "filter": {
                "property": "Store URL",
                "url": {
                    "contains": entry.store_url
                }
            }
        })
    
    def add_product_entry(self, entry: GShopEntry, variation: str):
        properties = dict()
        properties["Store"] = NDatabaseProperty.title(f'{entry.store_name} [{variation}]')
        properties["Color"] = NDatabaseProperty.select(variation)
        properties["Detail"] = NDatabaseProperty.rich_text(entry.details)
        properties["Price"] = NDatabaseProperty.number(entry.price)
        properties["Store URL"] = NDatabaseProperty.url(entry.store_url)

        args = dict()
        args["parent"] = { "database_id": self.database_id }
        args["properties"] = properties
        
        self.notion.pages.create(**args)

    def update_product_price(self, page_id: str, price_property_id: str, new_price: float):
        properties = dict()
        properties["Price"] = NDatabaseProperty.number(new_price)
        properties["Price"]["id"] = price_property_id

        args = dict()
        args["properties"] = properties

        self.notion.pages.update(page_id=page_id, **args)