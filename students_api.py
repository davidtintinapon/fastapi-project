from fastapi import FastAPI, HTTPException
from models import Student

app = FastAPI()
students = []

@app.post("/students", status_code=201)
def create_student(student: Student):
    students.append(student)
    return {"message": "Estudiante creado", "student": student}

@app.get("/students")
def view_student():
    return {"students": students}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if not (0 <= student_id < len(students)):
        raise HTTPException(status_code=404, detail="Estudiante no encontrado") 
    return {"student": students[student_id]}
    
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if not (0 <= student_id < len(students)):
        raise HTTPException(status_code=404, detail="Estudiante no encontrado") 
    students.pop(student_id)
    return {"message": "Estudiante eliminado"}
    
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if not (0 <= student_id < len(students)):
        raise HTTPException(status_code=404, detail="Estudiante no encontrado") 
    students[student_id] = student
    return {"message": "Estudiante modificado"} 