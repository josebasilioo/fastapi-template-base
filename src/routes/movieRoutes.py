# from fastapi import APIRouter
# from src.controllers.movieController import movieFunctions

# movies = APIRouter()

# @movies.get(movieFunctions.index('/', response_model=List[Movie]))
# @movies.post(movieFunctions.add_movie('/', status_code=201))
# @movies.put(movieFunctions.update_movie('/{id}'))
# @movies.delete(movieFunctions.delete_movie('/{id}'))