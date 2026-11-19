from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configuración de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuración de plantillas
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"title": "Cristóbal Farías — Desarrollador Full Stack"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
