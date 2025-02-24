## API Documentation
Simple REST API built in FastAPI to manage trade orders.

### Base URL
- **Local:** `http://localhost:8000`
- **Deployed:** `http://your-ec2-ip:8080`

### Endpoints

#### 📌 `GET /orders`
- **Description:** Fetch all trade orders
- **Response:**
  ```json
  [
    {"id": 1, "name": "AAPL", "quantity": 10, "price": 150.0},
    {"id": 2, "name": "TSLA", "quantity": 5, "price": 700.0}
  ]

#### 📌 `POST /orders`
- **Description:** Create a new trade order
- **Request:**
  ```json
  {"name": "AAPL", "quantity": 10, "price": 150.0}
  ```
- **Response:**
  ```json
  {"id": 1, "name": "AAPL", "quantity": 10, "price": 150.0}
  ```


