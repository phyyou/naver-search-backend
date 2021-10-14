from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.search import Search
from app.schemas.search import SearchCreate, SearchUpdate


class CRUDSearch(CRUDBase[Search, SearchCreate, SearchUpdate]):
    pass

search = CRUDSearch(Search)
