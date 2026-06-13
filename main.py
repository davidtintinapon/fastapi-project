from fastapi import FastAPI

app = FastAPI()

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