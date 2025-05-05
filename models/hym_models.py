from pydantic import BaseModel

class Producto_Base(BaseModel):
    nombre: str
    precio: str
    imagen: str
    