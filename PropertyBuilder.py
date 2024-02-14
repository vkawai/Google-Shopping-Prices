from Notion.NDatabaseProperty import NDatabaseProperty
from Google.GShopEntry import GShopEntry
from typing import Callable

class PropertyBuilder:
    function_builder: Callable[[str, GShopEntry], dict]

    def __init__(self, function_builder: Callable) -> None:
        self.function_builder = function_builder