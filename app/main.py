from fastapi import FastAPI
from app.routes.service import router as service_router
from app.config import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise
from app.routes.user import router as user_router
from app.routes.order import router as order_router
from tortoise import Tortoise
import asyncio

app  = FastAPI();

app.include_router(service_router, tags=["Service"])
app.include_router(user_router, tags=["User"])
app.include_router(order_router, tags=["Order"])    



register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)