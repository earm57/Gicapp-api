from pydantic import BaseModel
from datetime import datetime

class Consulta_compra(BaseModel):
    id_compra: int
    fecha: str
    cedula: int
    id_producto: int
    producto: str
    cantidad: int
    valor_total: float