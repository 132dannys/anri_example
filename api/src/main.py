from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from adminsite import site
from auth.base_config import fastapi_users, auth_backend
from auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="Anri App"
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

site.mount_app(app)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


@app.get("/")
async def debug():
    return {"Hello": "World!"}
