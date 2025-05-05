from fastapi import FastAPI
from routes.hym_routes import router as hym_router

app = FastAPI()

#router de productos
app.include_router(hym_router, prefix="/hym", tags=["hym"])

@app.get("/")
def read_root():
    return {"Hello": "World"}