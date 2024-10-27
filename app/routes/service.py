from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.service import Service
from pydantic import BaseModel


router = APIRouter()

@router.get("/services")
async def get_services():
    services = await Service.all()
    return services



class ServiceCreate(BaseModel):
    name: str
    description: str
    price: float

@router.post("/services")
async def create_service(service_data: ServiceCreate):
    service = Service(
        name=service_data.name,
        description=service_data.description,
        price=service_data.price
    )
    await service.save()
    return service 
