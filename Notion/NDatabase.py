from Notion.NDatabaseProperty import NDatabaseProperty
from Google.GShop import GShopEntry
from PropertyBuilder import PropertyBuilder
from notion_client import Client
from typing import Callable

class NDatabase:
    def __init__(self, client: Client, database_id: str) -> None:
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
    
    def add_entry(self, properties: dict):
        args = dict()
        args["parent"] = { "database_id": self.database_id }
        args["properties"] = properties
        self.notion.pages.create(**args)

    def update_entry(self, entry_id: str, properties: dict):
        args = dict()
        args["properties"] = properties
        self.notion.pages.update(page_id=entry_id, **args)