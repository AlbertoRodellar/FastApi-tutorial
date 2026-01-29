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


# Crea nuevo usuario en la array
@app.post("/user/")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "Usuario con ese id ya existe"}
    users_list.append(user)
    return user

# Actualiza usuario creado de la array
@app.put("/user/")
async def update_user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado usuario"}
    return user

# Elimina usuario de la array
@app.delete("/user/{id}")
async def delete_user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado usuario"}
    return {"mensaje": f"Usuario con id: {id} borrado"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado usuario"}