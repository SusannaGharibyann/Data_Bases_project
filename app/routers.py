from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, database, crud

router = APIRouter()

@router.post("/", response_model=schemas.Sport)
def create_sport(sport: schemas.SportCreate, db: Session = Depends(database.get_db)):
    return crud.create_sport(db, sport)

@router.get("/", response_model=list[schemas.Sport])
def get_sports(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_sports(db, skip=skip, limit=limit)

@router.get("/{sport_id}", response_model=schemas.Sport)
def get_sport(sport_id: int, db: Session = Depends(database.get_db)):
    return crud.get_sport(db, sport_id)

@router.put("/{sport_id}", response_model=schemas.Sport)
def update_sport(sport_id: int, sport: schemas.SportCreate, db: Session = Depends(database.get_db)):
    return crud.update_sport(db, sport_id, sport)

@router.delete("/{sport_id}", response_model=schemas.Sport)
def delete_sport(sport_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_sport(db, sport_id)
