from pydantic import BaseModel

class Crear_cliente(BaseModel):
    cedula: int
    nombre: str
    telefono: int
    correo: str
    direccion: str
    ciudad: str

class Mostrar_cliente(BaseModel):
    cedula: int
    nombre: str
    telefono: int
    correo: str
    direccion: str
    ciudad: str