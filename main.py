from fastapi import FastAPI, Body
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
    },
    {
        "id": 3,
        "title": "A Nightmare on Elm Street",
        "overview": "Un grupo de adolescentes es acosado en sus sueños por un asesino con una mano de cuchillas, que se manifiesta en la realidad.",
        "year": 1984,
        "rating": 7.5
    },
    {
        "id": 4,
        "title": "Texas Chainsaw Massacre",
        "overview": "Un grupo de amigos se encuentra con una familia de caníbales y un sádico asesino en una remota granja en Texas.",
        "year": 1974,
        "rating": 7.5
    },
    {
        "id": 4,
        "title": "It",
        "overview": "Un grupo de amigos en un pequeño pueblo se enfrenta a un antiguo mal en forma de un payaso aterrador que se alimenta de sus miedos más profundos.",
        "year": 2017,
        "rating": 7.8
    },
    {
        "id": 5,
        "title": "The Exorcist",
        "overview": "Una madre desesperada busca la ayuda de un sacerdote para expulsar un demonio que ha poseído a su hija.",
        "year": 1973,
        "rating": 8.0
    },
    {
        "id": 6,
        "title": "The Descent",
        "overview": "Un grupo de amigas se adentra en una cueva no explorada, donde descubren criaturas horribles y deben luchar por sobrevivir.",
        "year": 2005,
        "rating": 7.2
    },
    {
        "id": 7,
        "title": "The Invisible Man",
        "overview": "Una mujer que sospecha que su abusivo exnovio ha fingido su propia muerte para acosarla comienza a sospechar que está siendo acechada por una presencia invisible.",
        "year": 2020,
        "rating": 7.1
    },
    {
    "id": 8,
    "title": "The Shining",
    "overview": "Un escritor se muda con su familia a un hotel aislado en las montañas, donde descubre que la presencia sobrenatural del lugar lo está llevando a la locura.",
    "year": 1980,
    "rating": 8.4
    }, 
    {
    "id": 9,
    "title": "Wrong Turn",
    "overview": "Un grupo de jóvenes queda atrapado en el bosque de West Virginia, donde se encuentran con una familia de caníbales deformes que los acecha y los mata uno por uno.",
    "year": 2003,
    "rating": 6.1
    },
    {
    "id": 32,
    "title": "Jeepers Creepers",
    "overview": "Durante un viaje por carretera, dos hermanos descubren a un siniestro ser que se alimenta de seres humanos y que despierta cada 23 años para cazar a sus víctimas.",
    "year": 2001,
    "rating": 6.2
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

@app.get('/movies/{id}', tags=["Movies"])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies_list if item ['category'] == category]

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

