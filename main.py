from fastapi import FastAPI

from src.Demedia import Debmedia
from src.DisplayParser import DisplayParser

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/llamador/")
def fake_entry(consultorio: str, display: str, token: str, nombre: str):
    display = DisplayParser().parse(pantallas=display)
    Debmedia().fake_entry(consultorio, nombre, token, display)
    return None
