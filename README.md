# FastAPI Tutorial

Tutorial completo de FastAPI con ejemplos prácticos de diferentes funcionalidades del framework.

## 📋 Características

- **CRUD básico** con usuarios y productos
- **Integración con MongoDB** para persistencia de datos
- **Autenticación básica** con OAuth2
- **Autenticación JWT** con tokens seguros y contraseñas hasheadas (bcrypt)
- **APIRouter** para organizar endpoints
- **Validación de datos** con Pydantic

## 🚀 Estructura del Proyecto

```
├── routers/
│   ├── products.py          # Endpoints de productos
│   ├── users.py             # CRUD de usuarios en memoria
│   ├── users_db.py          # CRUD de usuarios con MongoDB
│   ├── basic_auth_users.py  # Autenticación básica OAuth2
│   └── jwt_auth_users.py    # Autenticación con JWT
├── db/
│   ├── client.py            # Configuración cliente MongoDB
│   ├── models/user.py       # Modelo Pydantic de usuario
│   └── schemas/user.py      # Schemas para transformar datos MongoDB
└── main.py                  # Archivo principal de la aplicación
```

## 🛠️ Tecnologías

- **FastAPI** - Framework web moderno y rápido
- **Pydantic** - Validación de datos
- **MongoDB** - Base de datos NoSQL
- **PyMongo** - Driver de MongoDB para Python
- **python-jose** - Manejo de JWT
- **passlib** - Hash de contraseñas con bcrypt
- **OAuth2** - Protocolo de autenticación

## 📦 Instalación

```bash
# Instalar dependencias
pip install fastapi uvicorn pymongo python-jose passlib python-multipart bcrypt

# Ejecutar la aplicación
uvicorn main:app --reload
```

## 🔐 Autenticación

### Basic Auth
- Usuario de prueba: `berudev` / `123456`
- Endpoint: `/login`

### JWT Auth
- Usuario de prueba: `berudev` / `123456` (hasheado en BD)
- Endpoint: `/login-jwt`
- Duración del token: 1 minuto

## 📚 Endpoints Principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/products` | Lista de productos |
| GET | `/users` | Lista de usuarios (memoria) |
| POST | `/users` | Crear usuario |
| PUT | `/users` | Actualizar usuario |
| DELETE | `/users/{id}` | Eliminar usuario |
| GET | `/userdb` | Lista de usuarios (MongoDB) |
| POST | `/login` | Login básico OAuth2 |
| POST | `/login-jwt` | Login con JWT |
| GET | `/users-jwt/me` | Usuario autenticado actual |

## 📝 Notas

- Los usuarios en `/users` se guardan en memoria (se pierden al reiniciar)
- Los usuarios en `/userdb` se persisten en MongoDB local
- Las contraseñas JWT están hasheadas con bcrypt
- El SECRET para JWT debería estar en un archivo `.env` en producción

## 🎓 Aprendizajes Clave

Este tutorial cubre:
- Creación de routers modulares
- Diferentes tipos de autenticación
- Integración con MongoDB (conexión, CRUD, schemas)
- Manejo de excepciones HTTP
- Validación de modelos con Pydantic
- Hash de contraseñas
- Generación y validación de JWT
- Uso de ObjectId de MongoDB

## 🎥 Videotutorial

Basado en el curso de FastAPI de MoureDev:  
[▶️ Ver en YouTube](https://youtu.be/_y9qQZXE24A?si=Rq3bP4owRaGgj73r)

---

**Autor:** Alberto Rodellar  
**Propósito:** Tutorial educativo de FastAPI
