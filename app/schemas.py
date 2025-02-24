from pydantic import BaseModel, Field
from datetime import datetime


class OrderCreate(BaseModel):
    symbol: str = Field(..., min_length=1, max_length=10, regex="^[A-Z]+$")
    quantity: int = Field(..., gt=0, description="Quantity must be a positive integer")
    price: float = Field(..., gt=0, description="Price must be a positive float")



class OrderResponse(OrderCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
