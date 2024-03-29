from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class ItemCreateRequest(ItemBase):
    title: str


# Properties to receive on item update
class ItemUpdateRequest(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class ItemResponse(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDBItemResponse(ItemInDBBase):
    pass
