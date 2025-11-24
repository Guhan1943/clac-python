from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Calculator API")

class Numbers(BaseModel):
    a: float
    b: float


@app.post("/add")
def add(nums: Numbers):
    return {"result": nums.a + nums.b}


@app.post("/subtract")
def subtract(nums: Numbers):
    return {"result": nums.a - nums.b}


@app.post("/multiply")
def multiply(nums: Numbers):
    return {"result": nums.a * nums.b}


@app.post("/divide")
def divide(nums: Numbers):
    if nums.b == 0:
        return {"error": "Cannot divide by zero!"}
    return {"result": nums.a / nums.b}


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Calculator!"}
