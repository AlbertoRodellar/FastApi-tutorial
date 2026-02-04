from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
#Clase objectId del Mongo
from bson import ObjectId
from bson.errors import InvalidId

router = APIRouter(prefix="/userdb",
                    tags=["userdb"],
                    responses={status.HTTP_404_NOT_FOUND: {"message":"No encontrado"}})

users_list = []

@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.local.users.find())

@router.get("/{id}")
async def user(id: str):
    user = search_user("_id", parse_object_id(id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user

@router.get("/")
async def user(id: str):
    user = search_user("_id", parse_object_id(id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya existe")
    
    # Transforma user en diccionario para añadirlo a Mongo
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id
    # Mongo crea automaticamente el campo _id
    new_user = search_user("_id", id)

    return new_user

@router.put("/", response_model=User)
async def update_user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.local.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario no actualizado")
        
    return search_user("_id", ObjectId(user.id))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    found = db_client.local.users.find_one_and_delete({"_id": parse_object_id(id)})

    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")


def search_user(field: str, key):
    # Acceder a base de datos: Cliente Mongo -> DB (local) -> colección (users) -> buscamos por email
    # Flujo Mongo: client → database → collection → query
        user = db_client.local.users.find_one({field: key})

        if not user:
            return None
        
        return User(**user_schema(user))

# Funcion helper por si error de id
def parse_object_id(id: str):
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Id invalida")
    
