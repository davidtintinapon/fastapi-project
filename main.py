from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    career: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/people")
def people():
    return {"people":[
        {"name": "Juan"},
        {"name": "Marco"}
    ]}

@app.get("/study")
def course():
    return {"course": "FastAPI", "level": "Beginner"}

@app.get("/people/{person_id}")
def get_people(person_id : int):
    return {"person_id": person_id, "message": "Estudiante encontrado"}

@app.post("/students")
def create_student(student: Student):
    return {"message": "Estudiante creado", "student": student}