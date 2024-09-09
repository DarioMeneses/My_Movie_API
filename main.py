from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'Mi aplicacion con FastAPI'
app.version = "0.0.1"
movies_list = [
    {
        "id": 1,
        "title": "Saw",
        "overview": "Un asesino en serie pone a sus victimas a prueba en juegos macabros donde deben salvar sus vidas",
        "year": 2004,
        "rating": 7.5
    },
    {
        "id": 2,
        "title": "Halloween",
        "overview": "El asesino Michael Myers escapa de un hospital psiquiatrico para asesinar a su hermana y aterrorizar a su antiguo pueblo",
        "year": 1978,
        "rating": 7.8
    }
]
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