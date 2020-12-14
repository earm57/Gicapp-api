from typing import Dict
from pydantic import BaseModel

class Cliente (BaseModel):
    cedula: int
    nombre: str
    telefono: int
    correo: str
    direccion: str
    ciudad: str

bd_cliente = Dict[int, Cliente]

bd_cliente = {
    1090366245: Cliente(**{ "cedula": 1090366245,
                            "nombre":"Ernesto Rincón",
                            "telefono": 3001234564,
                            "correo": "earm@gmail.com",
                            "direccion": "calle 0 # 20-45 La palmita",
                            "ciudad": "Villa del Rosario"}),
    1111623451: Cliente(**{ "cedula":1111623451,
                            "nombre": "Alejandro Mora",
                            "telefono": 3102154233,
                            "correo": "alemora@outlook.com",
                            "direccion": "Av. 20 # 45-12 Quinta Bosh",
                            "ciudad": "Cúcuta"}),
}

def obtener_cliente(cedula:int):
    if cedula in bd_cliente.keys():
        return bd_cliente[cedula]
    else:
        return None

def actualizar_cliente(clientedb: Cliente):
    bd_cliente[clientedb.cedula] = clientedb
    return clientedb

# def nuevo_cliente(clientedb: Cliente):
#     bd_cliente[clientedb.cedula] = clientedb
#     return True


