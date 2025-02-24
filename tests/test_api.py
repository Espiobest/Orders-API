import pytest
from sqlmodel import Session, create_engine
from app.main import app
from app.database import get_db
from app.models import Base
from fastapi.testclient import TestClient

TEST_DB = "sqlite:///./trades.db"
engine = create_engine(TEST_DB)


def override_get_db():
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def setup_db():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.mark.asyncio
async def test_create_order():

    response = client.post(
        "/orders",
        json={"symbol": "AAPL", "quantity": 10, "price": 100.0},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["symbol"] == "AAPL"
    assert data["quantity"] == 10
    assert data["price"] == 100.0
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_get_orders_empty():
    response = client.get("/orders")
    assert response.status_code == 200
    data = response.json()
    assert data == []


@pytest.mark.asyncio
async def test_get_orders():
    response1 = client.post(
            "/orders",
            json={"symbol": "AAPL", "quantity": 10, "price": 100.0},
        )
    response2 = client.get("/orders")
    assert response2.status_code == 200
    data = response2.json()
    assert len(data) == 1
    assert data[0]["symbol"] == "AAPL"
    assert data[0]["quantity"] == 10
    assert data[0]["price"] == 100.0
    assert data[0]["id"] == 1

