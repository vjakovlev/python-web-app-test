from pydantic import BaseModel

class OrderCreate(BaseModel):
    pizza_id: int
    quantity: int