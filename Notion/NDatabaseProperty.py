
class NDatabaseProperty:
    def title(text: str):
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
    
    def select(name: str):
        return {
            "type": "select",
            "select": {
                "name": name
            }
        }
    
    def rich_text(text: str):
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
    
    def number(number: str):
        return {
            "type": "number",
            "number": number
        }
    
    def url(url_string: str):
        return {
            "type": "url",
            "url": url_string
        }
    