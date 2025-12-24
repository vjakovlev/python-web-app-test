from app.models.pizza import Pizza
from app.schemas.pizza import PizzaCreate
from app.database import SessionLocal

db = SessionLocal()

def create_pizza(pizza: PizzaCreate):
    db_pizza = Pizza(**pizza.dict())
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza

def list_pizzas():
    return db.query(Pizza).all()