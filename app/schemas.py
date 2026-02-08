from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str
    full_name: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: Optional[int] = Field(default=1, ge=1, le=5)
    due_date: Optional[datetime] = None
    completed: Optional[bool] = False

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    due_date: Optional[datetime] = None
    priority: int
    owner: UserResponse

    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = Field(default=None, ge=1, le=5)
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None

class Login(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str