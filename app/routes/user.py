from fastapi import APIRouter

from app.models.user import User
from pydantic import BaseModel

router = APIRouter()

@router.get("/users")
async def get_users():
    users = await User.all()
    return users

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await User.get(id=user_id)
    return user

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    phone: str

@router.post("/users")
async def create_user(user: UserCreate):
    user = User(
        name=user.name,
        email=user.email,
        password=user.password,
        phone=user.phone
    )
    await user.save()
    return user


@router.get("/users/{user_id}/orders")
async def get_user_orders(user_id: int):
    user = await User.get(id=user_id)
    orders = await user.orders
    orders_with_services = []
    for order in orders:
        service = await order.service
        orders_with_services.append({
            "service_name": service.name,
            "service_description": service.description
        })
    return orders_with_services