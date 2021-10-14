from typing import Optional
from datetime import datetime

from pydantic import BaseModel


# Shared properties
class SearchBase(BaseModel):
    keyword: Optional[str] = None
    created_at: Optional[datetime] = None


# Properties to receive on item creation
class SearchCreate(SearchBase):
    keyword: str
    created_at: Optional[datetime] = datetime.now()


# Properties to receive on item update
class SearchUpdate(SearchBase):
    pass


# Properties shared by models stored in DB
class SearchInDBBase(SearchBase):
    id: int
    keyword: str
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Search(SearchInDBBase):
    pass


# Properties properties stored in DB
class SearchInDB(SearchInDBBase):
    pass
