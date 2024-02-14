
class NDatabaseProperty:
    def title(text: str) -> dict:
        return {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": text
                    }
                }
            ]
        }
    
    def select(name: str) -> dict:
        return {
            "type": "select",
            "select": {
                "name": name
            }
        }
    
    def rich_text(text: str) -> dict:
        return {
            "type": "rich_text",
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": text
                    }
                }
            ]
        }
    
    def number(number: float) -> dict:
        return {
            "type": "number",
            "number": number
        }
    
    def url(url_string: str) -> dict:
        return {
            "type": "url",
            "url": url_string
        }
    