from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books = [
    {
    "id" : 1,
    "title" : "The Alchemist",
    "author" : "Paulo Coelho"
    },
    {
    "id" : 2,
    "title" : "The God small things",
    "author" : "Arundhati Roy"
    },
    {
    "id" : 3,
    "title" : "The white Tiger",
    "author" : "Arvind Adiga "
    },
    {
    "id" : 4,
    "title" : "The place of illusions",
    "author" : "Chitra"
    },
]

app = FastAPI()

@app.get("/book")
def get_book():
    return books

class Book(BaseModel):
    id : int
    title : str
    author : str

# It is a pydantic function used to convert a model object into a dictionary  
@app.post("/book")
def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return {"message": "Book added", "book": new_book}

@app.get("/book/{book_id}")
def get_book(book_id : int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="Book Not Found")

class BookUpdate(BaseModel):
    title : str
    author : str

@app.put("/book/{book_id}")
def update_book(book_id : int, book_update : BookUpdate):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            return book
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found")
    
@app.delete("/book/{book_id}")
def delete(book_id : int):
    for book in books:
        if book['id'] ==book_id:
            books.remove(book)
            return {"Message" : "Book Deleted"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Book Not Found")