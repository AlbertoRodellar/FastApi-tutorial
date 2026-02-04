# Esta funcion es para convertir lo que nos devuelve la bbdd a nuestro objeto User
# Mongo (datos sucios)
#      ↓
# Schema (limpia / adapta)
#      ↓
# Modelo (valida / estructura)
#      ↓
# FastAPI responde

def user_schema(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"]
    }

def users_schema(users) -> list:
    return [user_schema(user) for user in users]