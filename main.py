from fastapi import FastAPI

from src.controllers.movieController import movies

app = FastAPI()

app.include_router(movies)