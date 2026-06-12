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