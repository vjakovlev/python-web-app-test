from fastapi import APIRouter, Depends
from app.services.pizza_service import create_pizza, list_pizzas
from app.schemas.pizza import PizzaCreate
from app.routers.order import get_current_user

router = APIRouter(prefix="/pizzas", tags=["pizzas"])

@router.post("/")
def add_pizza(pizza: PizzaCreate):
    return create_pizza(pizza)

@router.get("/")
def get_pizzas(current_user: str = Depends(get_current_user)):
    return list_pizzas()