from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='app/templates')
# Mock data representing Colombian teams
teams =[
    {"id": 1, "name": "Atlético Nacional", "city": "Medellín"},
    {"id": 2, "name": "Millonarios", "city": "Bogotá"},
    {"id": 3, "name": "América de Cali", "city": "Cali"},
    {"id": 4, "name": "Junior", "city": "Barranquilla"}
]

@app.get("/", response_class=HTMLResponse)
async def read_teams(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "teams": teams})
