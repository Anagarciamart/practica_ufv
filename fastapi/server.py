from fastapi import FastAPI
import pandas as pd
from typing import List

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class Libro(BaseModel):
    id_libro: int
    libro_nombre: str
    numpaginas: int
    libro_raiting_promedio: float
    fechapublicacion: str
    id_editorial: int
    libro_review_counts: int
    id_idioma: int
    id_autor: int
    ISBN: int
    idioma: str
    autor_genero: str
    autor: str
    id_pais: int
    autor_rating_promedio: float
    pais: str
    editorial: str


class ListadoLibros(BaseModel):
    libros = List[Libro]


app = FastAPI(
    title="Servidor de datos",
    description="""Datos de libros""",
    version="0.1.0",
)


@app.get("/retrieve_data/")
def retrieve_data():
    todosmisdatos = pd.read_csv('Libros.csv', sep='|')
    todosmisdatos = todosmisdatos.fillna(0)
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = ListadoLibros()
    listado.libros = todosmisdatosdict
    return listado
