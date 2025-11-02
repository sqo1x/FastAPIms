from pydantic import BaseModel, EmailStr, Field
from typing import Annotated


class CreateUser(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=64)
