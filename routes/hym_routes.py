from fastapi import APIRouter
from models.hym_models import Producto_Base
from services.hym_service import get_hym_camisas, get_hym_jeans

router = APIRouter()

@router.get("/prueba")
async def prueba():
    return {"message": "Hello, prueba!"}

@router.get("/camisas",response_model=list[Producto_Base])
async def get_camisas(): 
    return get_hym_camisas()

@router.get("/jeans",response_model=list[Producto_Base])
async def get_camisas(): 
    return get_hym_jeans()
