from fastapi import FastAPI
from models.hym_models import Producto_Base
from bs4 import BeautifulSoup
import requests


# Esta funcion hace el scrapping de la pagina web de hym
def get_hym_productos(categoria: str):
    
    #url de la pagina web de hym que recibe la categoria como parametro 
    url = f"https://co.hm.com/hombre/{categoria}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)    
    soup = BeautifulSoup(response.content, "html.parser")
    productos = []
    
    #Este es el div principal donde se encuentran los productos
    for quote_block in soup.find_all("div", class_ ="vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--grid pa4"):
        #aca se busca el nombre del producto
        nombre_producto = quote_block.find("span", class_="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body").text
        print (nombre_producto)
        
        #aca se busca el precio del producto
        precio_producto = quote_block.find("span", class_="vtex-product-price-1-x-sellingPriceValue vtex-product-price-1-x-sellingPriceValue--newlistPrice").text
        print("Precio del producto:", precio_producto)

        #aca se busca la imagen del producto
        imagen_producto = quote_block.find("img", class_="vtex-product-summary-2-x-imageNormal vtex-product-summary-2-x-image vtex-product-summary-2-x-image--commonImage vtex-product-summary-2-x-mainImageHovered vtex-product-summary-2-x-mainImageHovered--commonImage").get("src")
        print("Imagen del producto:", imagen_producto)
        
        productos.append(
            Producto_Base(
                nombre=nombre_producto,
                precio=precio_producto,
                imagen=imagen_producto
            )
        )
        
    return productos

