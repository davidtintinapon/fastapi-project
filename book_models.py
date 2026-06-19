from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    year: int = Field(gt=1000, lt=2027)