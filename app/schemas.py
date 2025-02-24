from pydantic import BaseModel
from datetime import datetime


class OrderCreate(BaseModel):
    symbol: str
    price: float
    quantity: int


class OrderResponse(OrderCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
