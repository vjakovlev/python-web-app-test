from fastapi import FastAPI
from app.routers import auth, pizza, order
from app.database import Base, engine

app = FastAPI(
    title="🍕 Pizza Ordering API",
    description="Order your favorite pizzas here!",
    version="1.0",
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(auth.router)
app.include_router(pizza.router)
app.include_router(order.router)