from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Sport(Base):
    tablename = "sports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    unit = Column(String, nullable=False)
    world_record = Column(Float, nullable=True)
    olympic_record = Column(Float, nullable=True)

    results = relationship("Result", back_populates="sport")

class Athlete(Base):
    tablename = 'athletes'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
    victories = Column(Integer, default=0)

    results = relationship("Result", back_populates="athlete")

class Result(Base):
    tablename = "results"

    id = Column(Integer, primary_key=True, index=True)
    competition_name = Column(String, nullable=False)
    performance = Column(Float, nullable=False)
    event_date = Column(String, nullable=False)
    location = Column(String, nullable=False)
    sport_id = Column(Integer, ForeignKey("sports.id"))
    athlete_id = Column(Integer, ForeignKey("athletes.id"))

    sport = relationship("Sport", back_populates="results")
    athlete = relationship("Athlete", back_populates="results")