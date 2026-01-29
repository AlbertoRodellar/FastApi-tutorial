from fastapi import FastAPI

app = FastAPI()

# Iniciar servidor: uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc