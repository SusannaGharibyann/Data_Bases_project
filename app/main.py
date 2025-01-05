from fastapi import FastAPI
from .database import Base, engine
from .routers import sports, athletes, results

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add routers
app.include_router(sports.router, prefix="/sports", tags=["sports"])
app.include_router(athletes.router, prefix="/athletes", tags=["athletes"])
app.include_router(results.router, prefix="/results", tags=["results"])
