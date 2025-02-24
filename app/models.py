from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

from datetime import datetime

Base = declarative_base()


class Order(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    symbol = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Order {self.symbol} {self.quantity} {self.price}>"
