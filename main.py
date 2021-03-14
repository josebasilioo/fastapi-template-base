from fastapi import FastAPI
from src.database import metadata, database, engine
from src.routes.movieRoutes import movies

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies)
