from pydantic import BaseModel
from typing import Optional

# Схемы для списков
class ListBase(BaseModel):
    name: str

class ListCreate(ListBase):
    pass

class List(ListBase):
    id: int
    
    class Config:
        from_attributes = True

# Схемы для ссылок
class LinkBase(BaseModel):
    url: str
    title: str
    description: Optional[str] = None
    list_id: Optional[int] = None

class LinkCreate(LinkBase):
    pass

class Link(LinkBase):
    id: int
    
    class Config:
        from_attributes = True