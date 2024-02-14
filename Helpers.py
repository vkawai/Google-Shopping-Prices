from Google.GShopEntry import GShopEntry
from Notion.NDatabaseProperty import NDatabaseProperty

def case_properties(entry: GShopEntry, variant: str) -> dict:
    properties = dict()
    properties["Store"] = NDatabaseProperty.title(f'{entry.store_name} [{variant}]')
    properties["Color"] = NDatabaseProperty.select(variant)
    properties["Detail"] = NDatabaseProperty.rich_text(entry.details)
    properties["Price"] = NDatabaseProperty.number(entry.price)
    properties["Store URL"] = NDatabaseProperty.url(entry.store_url)

    return properties

def gpu_properties(entry: GShopEntry, brand: str) -> dict:
    properties = dict()
    properties["Model"] = NDatabaseProperty.rich_text(entry.product_name)
    properties["Store"] = NDatabaseProperty.title(entry.store_name)
    properties["Brand"] = NDatabaseProperty.select(brand)
    properties["Detail"] = NDatabaseProperty.rich_text(entry.details)
    properties["Price"] = NDatabaseProperty.number(entry.price)
    properties["Store URL"] = NDatabaseProperty.url(entry.store_url)

    return properties

def update_price(price_property_id: str, new_price: float):
    properties = dict()
    properties["Price"] = NDatabaseProperty.number(new_price)
    properties["Price"]["id"] = price_property_id
    return properties
