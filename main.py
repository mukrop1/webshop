from fastapi import FastAPI, Body
import uvicorn
from pydantic import EmailStr, BaseModel

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello():
    return {"message": "Hello asa!"}


@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]

@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
