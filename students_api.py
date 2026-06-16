from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    career: str

students = []

@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"message": "Estudiante creado", "student": student}

@app.get("/students")
def view_student():
    return {"students": students}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if 0 <= student_id < len(students):
        return {"student": students[student_id]}
    else:
        return {"error": "Estudiante no encontrado"}
    
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if 0 <= student_id < len(students):
        students.pop(student_id)
        return {"message": "Estudiante eliminado"}

    else:
        return {"error": "Estudiante no encontrado"}