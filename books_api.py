from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    year: int = Field(gt=1000, lt=2027)

books = []

@app.post("/books", status_code=201)
def create_book(new_book: Book):
    books.append(new_book)
    return {"message": "Libro creado", "book": new_book}

@app.get("/books")
def view_books():
    return {"books": books}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if not (0 <= book_id < len(books)):
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"book": books[book_id]}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if not (0 <= book_id < len(books)):
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    books.pop(book_id)
    return {"message": "Libro eliminado"}
    
@app.put("/books/{book_id}")
def update_book(book_id: int, new_book: Book):
    if not (0 <= book_id < len(books)):
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    books[book_id] = new_book
    return {"message": "Libro modificado correctamente"}