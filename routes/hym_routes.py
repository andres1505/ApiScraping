from fastapi import APIRouter
from models.hym_models import Producto_Base
from services.hym_service import get_hym_productos

router = APIRouter()

@router.get("/prueba")
async def prueba():
    return {"message": "Hello, prueba!"}


#recibe la categoria y devuelve la lista de productos
@router.get("/{categoria}",response_model=list[Producto_Base])
def obtener_productos(categoria: str):
    return get_hym_productos(categoria)