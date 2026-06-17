from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int

books = []

@app.post("/books")
def create_book(new_book: Book):
    books.append(new_book)
    return {"message": "Libro creado", "book": new_book}

@app.get("/books")
def view_books():
    return {"books": books}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if 0 <= book_id < len(books):
        return {"book": books[book_id]}
    else:
        return {"error": "Libro no encontrado"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if 0 <= book_id < len(books):
        books.pop(book_id)
        return {"message": "Libro eliminado"}
    else:
        return {"error": "Libro no encontrado"}
    
@app.put("/books/{book_id}")
def update_book(book_id: int, new_book: Book):
    if 0 <= book_id < len(books):
        books[book_id] = new_book
        return {"message": "Libro modificado correctamente"}
    else:
        return {"error": "Libro no encontrado"}