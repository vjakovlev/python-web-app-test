from pydantic import BaseModel

class PizzaCreate(BaseModel):
    name: str
    description: str
    price: float

class PizzaOut(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True