from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "title": "Foo Fighters",
                "image": "https://linktomyimage.com/image.png",
                "description": "Foo Fighters in Inverness",
                "tags": ["Rock", "Music"],
                "location": "Eden Court",
            }
        }


class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Foo Fighters",
                "image": "https://linktomyimage.com/image.png",
                "description": "Foo Fighters in Inverness",
                "tags": ["Rock", "Music"],
                "location": "Eden Court",
            }
        }
