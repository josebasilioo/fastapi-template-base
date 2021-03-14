from fastapi import APIRouter
from src.controllers import movieController

movies = APIRouter()

movies.include_router(movieController.movies, prefix='/movies', tags=["movies"])