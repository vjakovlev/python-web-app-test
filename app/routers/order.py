from fastapi import APIRouter, Depends
from app.services.order_service import create_order
from app.schemas.order import OrderCreate
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.core.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
router = APIRouter(prefix="/orders", tags=["orders"])

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")
    if username is None:
        raise Exception("Invalid token")
    return username  # Ideally fetch from DB

@router.post("/")
def place_order(order: OrderCreate, username: str = Depends(get_current_user)):
    # Here you would map username to user_id
    user_id = 1  # Simulate for now
    return create_order(user_id, order)