from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    age: int = Field(gt=0, lt=120)
    career: str = Field(min_length=1, max_length=50)