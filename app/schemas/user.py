from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreateRequest(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdateRequest(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserResponse(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDBResponse(UserInDBBase):
    hashed_password: str
