from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, EmailStr
from enum import Enum

class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    email: EmailStr
    password: str
    username: str
    firstname: str
    lastname: str
    gender: Gender
    nationality: str
    dob: str
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    profileimg: str = "https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg"
    role: Optional[str]