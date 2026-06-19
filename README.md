# FastAPI Practice Projects

This repository contains two REST APIs built with FastAPI: a student management API and a book management API. Both projects implement full CRUD operations (Create, Read, Update, Delete) with data validation and proper HTTP status codes.

## Students API

Allows creating, listing, searching, updating and deleting students. Each student has a name, age, and career.

## Books API

Allows creating, listing, searching, updating and deleting books. Each book has a title, author, and publication year.

## Technologies

- Python
- FastAPI
- Pydantic

## How to run

1. Clone this repository
2. Activate the virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run the students API: `uvicorn students_api:app --reload`
5. Run the books API: `uvicorn books_api:app --reload`

## Features

- Input validation using Pydantic (field length and value ranges)
- Proper HTTP status codes (201 for created, 404 for not found)
- Error handling with HTTPException