from typing import Dict
from datetime import datetime
from pydantic import BaseModel


class Compra(BaseModel):
    id_compra: int
    fecha: str
    cedula: int
    id_producto: int
    producto: str
    cantidad: int
    valor_total: float
    
bd_compra = Dict[int, Compra]

bd_compra ={
    1:Compra(**{"id_compra": 1,
                "fecha": "2020-12-10",
                "id_producto": 1234,
                "cedula": 1090366245,
                "producto": "Carro control remoto",
                "cantidad": 1,
                "valor_total": 82500}),
    2:Compra(**{"id_compra": 2,
                "fecha": "2020-12-12",
                "cedula": 1111623451,
                "id_producto": 4321,
                "producto": "chromecast 4",
                "cantidad": 2,
                "valor_total": 450000}),
}

def obtener_compra(idcedula: int):
    for i in bd_compra:
        if idcedula == bd_compra[i].cedula:
            return bd_compra[i]
    else:
        print ("entro acá")
        return None
    