from pydantic import BaseModel
from fastapi_users import schemas
import uuid

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    title: str
    content: str

class UserRead(schemas.BaseUser[uuid.UUID]):
    username : str | None = None

class UserCreate(schemas.BaseUserCreate):
    username : str

class UserUpdate(schemas.BaseUserUpdate):
    username : str | None = None