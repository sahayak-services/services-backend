from fastapi import APIRouter
from app.models.order import Order
from pydantic import BaseModel


router = APIRouter()

@router.get("/orders")
async def get_orders():
    orders = await Order.all()
    return orders

@router.get("/orders/{order_id}")
async def get_order(order_id: int):
    order = await Order.get(id=order_id)
    return order

class OrderCreate(BaseModel):   
    user_id: int
    service_id: int

@router.post("/orders")
async def create_order(order: OrderCreate):
    order = Order(
        user_id=order.user_id,
        service_id=order.service_id
    )
    await order.save()
    return order

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    order = await Order.get(id=order_id)
    await order.delete()
    return order

@router.put("/orders/{order_id}")
async def update_order(order_id: int, order_data: OrderCreate):
    order = await Order.get(id=order_id)
    order.user_id = order_data.user_id
    order.service_id = order_data.service_id
    await order.save()
    return order

@router.get("/orders/{order_id}/service")
async def get_order_service(order_id: int):
    order = await Order.get(id=order_id)
    service = await order.service
    return service

@router.get("/orders/{order_id}/user")
async def get_order_user(order_id: int):
    order = await Order.get(id=order_id)
    user = await order.user
    return user

