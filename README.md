## Simple REST API built in FastAPI to manage trade orders.
## **🛠️ Setup & Deployment on AWS**
Follow these steps to deploy this FastAPI app on an AWS EC2 instance using **Docker & GitHub Actions**.

### **1️⃣ Create an EC2 Instance**
- Launch an **Ubuntu 22.04** EC2 instance.
- Open inbound ports **8080** (API) and **5432** (PostgreSQL) in Security Groups.
- SSH into the instance:
  ```sh
  ssh -i your-key.pem ubuntu@your-ec2-public-ip
  ```
### **2️⃣ Install Docker and PostgreSQL**
```shell
sudo apt update && sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
```
### **3️⃣ Clone the Repository**
```shell
git clone
cd Orders-API
```
### **4️⃣ Set Environment Variables**
- Create a `.env` file in the root directory:
  ```shell
  touch .env
  ```
- Add the following environment variables to the `.env` file:
  ```shell
  DB_URL=postgresql://your_username:your_password@your_ec2_publicIP/trades
  ```
### **5️⃣ Build and Run the Docker Container**
  ```shell
  docker-compose up -d --build
  ```


### Base URL
- **Local:** `http://localhost:8000`
- **Deployed:** `http://your-ec2-ip:8080`

## API Documentation
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


