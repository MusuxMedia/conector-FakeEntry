from fastapi import FastAPI, status
from .src import Debmedia
from .src import DisplayParser

app = FastAPI()


@app.get("/llamador/", status_code=status.HTTP_204_NO_CONTENT)
def fake_entry(consultorio: str, display: str, token: str, nombre: str = "", turno: str = "",
               server: str = "debqclients") -> None:
    display = DisplayParser().parse(pantallas=display)
    Debmedia().fake_entry(consultorio=consultorio, token=token, pantallas=display, paciente=nombre, turno=turno,
                          server=server)
