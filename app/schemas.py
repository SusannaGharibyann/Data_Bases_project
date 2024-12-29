from pydantic import BaseModel, Field
from typing import List, Optional

class ResultBase(BaseModel):
    competition_name: str
    performance: float
    event_date: str
    location: str
    sport_id: int
    athlete_id: int

class ResultCreate(ResultBase):
    pass

class Result(ResultBase):
    id: int

    class Config:
        orm_mode = True

class SportBase(BaseModel):
    name: str
    unit: str
    world_record: Optional[float] = None
    olympic_record: Optional[float] = None

class SportCreate(SportBase):
    pass

class Sport(SportBase):
    id: int
    results: List[Result] = Field(default_factory = List)
    class Config:
        orm_mode = True

class AthleteBase(BaseModel):
    full_name: str
    country: str
    birth_year: int
    victories: int

class AthleteCreate(AthleteBase):
    pass

class Athlete(AthleteBase):
    id: int
    results: List[Result] = Field(default_factory=list)

    class Config:
        orm_mode = True
