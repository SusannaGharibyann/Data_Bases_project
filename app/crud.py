from sqlalchemy.orm import Session
from . import models, schemas

# SPORTS
def create_sport(db: Session, sport: schemas.SportCreate):
    db_sport = models.Sport(**sport.dict())
    db.add(db_sport)
    db.commit()
    db.refresh(db_sport)
    return db_sport

def get_sport(db: Session, sport_id: int):
    return db.query(models.Sport).filter(models.Sport.id == sport_id).first()

def get_sports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sport).offset(skip).limit(limit).all()

def update_sport(db: Session, sport_id: int, sport: schemas.SportCreate):
    db_sport = db.query(models.Sport).filter(models.Sport.id == sport_id).first()
    if db_sport:
        for key, value in sport.dict().items():
            setattr(db_sport, key, value)
        db.commit()
        db.refresh(db_sport)
    return db_sport

def delete_sport(db: Session, sport_id: int):
    db_sport = db.query(models.Sport).filter(models.Sport.id == sport_id).first()
    if db_sport:
        db.delete(db_sport)
        db.commit()
    return db_sport


# ATHLETES
def create_athlete(db: Session, athlete: schemas.AthleteCreate):
    db_athlete = models.Athlete(**athlete.dict())
    db.add(db_athlete)
    db.commit()
    db.refresh(db_athlete)
    return db_athlete

def get_athlete(db: Session, athlete_id: int):
    return db.query(models.Athlete).filter(models.Athlete.id == athlete_id).first()

def get_athletes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Athlete).offset(skip).limit(limit).all()

def update_athlete(db: Session, athlete_id: int, athlete: schemas.AthleteCreate):
    db_athlete = db.query(models.Athlete).filter(models.Athlete.id == athlete_id).first()
    if db_athlete:
        for key, value in athlete.dict().items():
            setattr(db_athlete, key, value)
        db.commit()
        db.refresh(db_athlete)
    return db_athlete

def delete_athlete(db: Session, athlete_id: int):
    db_athlete = db.query(models.Athlete).filter(models.Athlete.id == athlete_id).first()
    if db_athlete:
        db.delete(db_athlete)
        db.commit()
    return db_athlete


# RESULTS
def create_result(db: Session, result: schemas.ResultCreate):
    db_result = models.Result(**result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_result(db: Session, result_id: int):
    return db.query(models.Result).filter(models.Result.id == result_id).first()

def get_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Result).offset(skip).limit(limit).all()

def update_result(db: Session, result_id: int, result: schemas.ResultCreate):
    db_result = db.query(models.Result).filter(models.Result.id == result_id).first()
    if db_result:
        for key, value in result.dict().items():
            setattr(db_result, key, value)
        db.commit()
        db.refresh(db_result)
    return db_result

def delete_result(db: Session, result_id: int):
    db_result = db.query(models.Result).filter(models.Result.id == result_id).first()
    if db_result:
        db.delete(db_result)
        db.commit()
    return db_result
