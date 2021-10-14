from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.param_functions import Body
from sqlalchemy.orm import Session

import requests

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Search])
def read_searches(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve searches.
    """
    searches = crud.search.get_multi(db, skip=skip, limit=limit)
    return searches

@router.get("/nate", response_model=Any)
def read_nate_ranks(
) -> Any:
    """
    Retrieve nate ranks.
    """
    return requests.get("https://test-api.signal.bz/news/realtime").json()


@router.post("/", response_model=schemas.Search)
def create_search(
    *,
    db: Session = Depends(deps.get_db),
    keyword: str = Body(...),
) -> Any:
    """
    Create new search.
    """
    search_in = schemas.SearchCreate(keyword=keyword)
    search = crud.search.create(db=db, obj_in=search_in)
    return search


@router.put("/{id}", response_model=schemas.Search)
def update_search(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    search_in: schemas.SearchUpdate,
) -> Any:
    """
    Update an search.
    """
    search = crud.search.get(db=db, id=id)
    if not search:
        raise HTTPException(status_code=404, detail="Search not found")
    search = crud.search.update(db=db, db_obj=search, obj_in=search_in)
    return search


@router.get("/{id}", response_model=schemas.Search)
def read_search(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get search by ID.
    """
    search = crud.search.get(db=db, id=id)
    return search


@router.delete("/{id}", response_model=schemas.Search)
def delete_search(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an search.
    """
    search = crud.search.get(db=db, id=id)
    if not search:
        raise HTTPException(status_code=404, detail="Search not found")
    search = crud.search.remove(db=db, id=id)
    return search
