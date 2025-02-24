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
### **6️⃣ Add secrets to Github**
This project uses GitHub Actions for auto-deployment to EC2.

Go to GitHub Repo → Settings → Secrets → Actions and add the following:

| Secret Name | Value (Example) |
|-------------|-----------------|
| EC2_HOST    | your-ec2-public-ip |
| EC2_USER    | ubuntu |
| EC2_SSH_KEY | Your private SSH key (cat ~/.ssh/id_rsa) |
| DOCKERHUB_USERNAME | Your Docker Hub username |
| DOCKERHUB_PASSWORD | Your Docker Hub password or access token |

### Base URL
- **Local:** `http://localhost:8000`
- **Deployed:** `http://your-ec2-ip:8080`

## API Documentation
After running the API, visit:

Swagger UI: http://localhost:8080/docs
Redoc: http://localhost:8080/redoc

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


