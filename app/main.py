from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import init_db, get_db
from .models import Order
from .schemas import OrderCreate, OrderResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()


@app.get("/orders", response_model=list[OrderResponse])
async def get_orders(db: Session = Depends(get_db)):
    try:
        return db.query(Order).all()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    if not order.symbol:
        raise HTTPException(status_code=400, detail="Symbol is required")
    db_order = Order(
        symbol=order.symbol,
        quantity=order.quantity,
        price=order.price,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
