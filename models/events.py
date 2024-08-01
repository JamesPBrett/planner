from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Foo Fighters",
                "image": "https://linktomyimage.com/image.png",
                "description": "Foo Fighters in Inverness",
                "tags": ["Rock", "Music"],
                "location": "Eden Court"
            }
        }
