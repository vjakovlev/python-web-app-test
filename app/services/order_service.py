from app.models.order import Order
from app.schemas.order import OrderCreate
from app.database import SessionLocal

db = SessionLocal()

def create_order(user_id: int, order: OrderCreate):
    db_order = Order(user_id=user_id, pizza_id=order.pizza_id, quantity=order.quantity)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order