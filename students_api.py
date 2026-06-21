from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student
from db_models import StudentDB
from database import get_db

app = FastAPI()

@app.post("/students", status_code=201)
def create_student(student: Student, db: Session = Depends(get_db)):
    new_student = StudentDB(name=student.name, age=student.age, career=student.career)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Estudiante creado", "student": new_student}

@app.get("/students")
def view_student(db: Session = Depends(get_db)):
    all_students = db.query(StudentDB).all()
    return {"students": all_students}

@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado") 
    return {"student": student}
    
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado") 
    db.delete(student)
    db.commit()
    return {"message": "Estudiante eliminado"}
    
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    existing_student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if existing_student is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.career = student.career
    db.commit()
    return {"message": "Estudiante modificado"}