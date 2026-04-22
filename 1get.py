from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"Message":"Hello World"}

@app.get("/about")
def about():
    return {"About":"Welcome to FastAPI tutorial"}

@app.get("/greet")
def greet():
    return {"Message":"Hello Sam"}

# Path Parameter : name
@app.get("/greet1/{name}")
def greet(name: str):
    return {"Message": f"Hello {name}"}

# Query Parameter : age
@app.get("/greet2/{name}")
def greet_name(name: str, age: int):
    return {"Message": f"Hello {name}, you are {age} years old."}

# To make Query Parameter optional
from typing import Optional
@app.get("/greet3/{name}")
def greet_name(name: str, age: Optional[int] = None):
    if age:
        return {"Message": f"Hello {name}, you are {age} years old."}
    return {"Message": f"Hello {name}"}



