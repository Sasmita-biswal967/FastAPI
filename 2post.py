from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create")
def create(student:Student):
    return {
        "name": student.name,
        "age": student.age,
        "roll": student.roll
    }
