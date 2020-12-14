from db.cliente_db import bd_cliente
from db.cliente_db import actualizar_cliente, obtener_cliente

from db.compra_db import bd_compra
from db.compra_db import obtener_compra

from models.cliente_models import Crear_cliente, Mostrar_cliente
from models.compra_models import Consulta_compra

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

gicapp_api = FastAPI()

@gicapp_api.get("/cliente/{cedula}")
async def get_cliente(cedula: int):
    clientedb = obtener_cliente(cedula)
    if clientedb == None:
        raise HTTPException (status_code=404, detail="cliente no existe")
    #cliente_consulta = Mostrar_cliente(**clientedb.dict())
    return clientedb #cliente_consulta

@gicapp_api.get("/cliente/compra/{cedula}")
async def get_compra(cedula: int):
    clientedb = obtener_cliente(cedula)
    if clientedb == None:
        raise HTTPException (status_code=404, detail="cliente no existe")
    compracliente = obtener_compra(cedula)
    return compracliente


@gicapp_api.post("/cliente/")
async def crear_cliente(clientenuevo: Crear_cliente):
    clientedb = obtener_cliente(clientenuevo.cedula)
    if clientedb != None:
        raise HTTPException(status_code=404,detail="El usuario ya existe con esa cédula")
    actualizar_cliente(clientenuevo)
    #aprobado = "Cliente creado con exito"
    return 