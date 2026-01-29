from fastapi import FastAPI
from pydantic import BaseModel

# Iniciar servidor: uvicorn users:app --reload

app = FastAPI()

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name="Beru", surname="Test", url="https://test.com", age=41),
        User(id=2,name="xd", surname="perri", url="https://xd.com", age=23),
        User(id=3,name="Chesi", surname="gato", url="https://gato.com", age=11)]

@app.get("/usersjson")
async def users():
    return [{"name": "Beru", "surname": "test", "url": "https://test.com", "age": 35},
            {"name": "XD", "surname": "perro", "url": "https://xd.com", "age": 22},
            {"name": "Chelsi", "surname": "gato", "url": "https://gato.com", "age": 24}]

# Lo devuelve con json, gracias al BaseModel
@app.get("/users")
async def users():
    return users_list

# Devuelve usuario por id, con un try except por si no lo encuentra

# Path -> /user/1
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Query -> /user/?id=1
@app.get("/user/")
async def user(id: int):
    return search_user(id)


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error", "No se ha encontrado usuario"}


