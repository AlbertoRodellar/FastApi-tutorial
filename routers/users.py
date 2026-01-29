from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Prefix para que todas las rutas de aqui sean /users 
# Tags para ordenar en la documentación
router = APIRouter(prefix="/users",
                    tags=["users"],
                    responses={404: {"message":"No encontrado"}})

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

@router.get("/usersjson")
async def users():
    return [{"name": "Beru", "surname": "test", "url": "https://test.com", "age": 35},
            {"name": "XD", "surname": "perro", "url": "https://xd.com", "age": 22},
            {"name": "Chelsi", "surname": "gato", "url": "https://gato.com", "age": 24}]

# Lo devuelve con json, gracias al BaseModel
@router.get("/")
async def users():
    return users_list

# Devuelve usuario por id, con un try except por si no lo encuentra

# Path -> /user/1
@router.get("/{id}")
async def user(id: int):
    return search_user(id)


# Query -> /user/?id=1
@router.get("/")
async def user(id: int):
    return search_user(id)


# Crea nuevo usuario en la array
@router.post("/", response_model=User, status_code=201)
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    
    users_list.append(user)
    return user

# Actualiza usuario creado de la array
@router.put("/")
async def update_user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Elimina usuario de la array
@router.delete("/{id}")
async def delete_user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": f"Usuario con id: {id} borrado"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado usuario"}
    