from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from movies_list import movies_list

app = FastAPI()
app.title = 'Mi aplicacion con FastAPI'
app.version = "0.0.1"

@app.get('/', tags=["Home"])
def message():
    #return {"Hello":"Dario"}
     return HTMLResponse ('<h1>Hello Dario</h1>')
@app.get('/movies', tags=["Movies"])
def movies():
    return movies_list 

@app.get('/movies/{id}', tags=["Movies"])
def get_movie(id: int):
    for item in movies_list:
        if item['id'] == id:
            return item
    return {"error": "Movie not found"}

@app.get('/movies/', tags=["Movies"])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies_list if item['year'] == year]

@app.post('/movies', tags=["Movies"])
def create_movie(id: int =Body(), title: str =Body(), overview: str =Body(), year: int =Body(), category: str =Body()):
    movies_list.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "category": category
    })
    return movies_list

@app.put('/movies/{id}', tags=["Movies"])
def update_movie(id: int, title: str =Body(), overview: str =Body(), year: int =Body(), rating: float =Body(), category: str =Body()):
     for item in movies_list:
        if item['id'] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category,
            return movies_list
     return {"error": "Movie not found"}    
        
@app.delete('/movies/{id}', tags=["Movies"])
def delete_movie(id: int):
     for item in movies_list:
        if item['id'] == id:
            movies_list.remove(item)
            return movies_list
     return {"error": "Movie not found"}