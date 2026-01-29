from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Beru", surname="Test", url="https://test.com", age=41),
        User(name="xd", surname="perri", url="https://xd.com", age=23),
        User(name="Chesi", surname="gato", url="https://gato.com", age=11)]

@app.get("/usersjson")
async def users():
    return [{"name": "Beru", "surname": "test", "url": "https://test.com", "age": 35},
            {"name": "XD", "surname": "perro", "url": "https://xd.com", "age": 22},
            {"name": "Chelsi", "surname": "gato", "url": "https://gato.com", "age": 24}]

@app.get("/users")
async def users():
    return users_list