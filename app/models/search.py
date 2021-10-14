from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Search(Base):
    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, index=True)
    created_at = Column(DateTime)
