# 🚀 Flask based Microservices Architecture using Docker in Docker

This project demonstrates a simple microservices architecture using **Docker Compose**. It includes three services:
- 🍭 `product-service`
- 📍 `order-service`
- 👤 `user-service`

Each service runs as an isolated container, built from lightweight Python (Flask) images.


## 🏗️ Project Structure
```
microservices-project/
│
├── docker-compose.yml
│
├── product-service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── order-service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── user-service/
    ├── app.py
    ├── Dockerfile
    └── requirements.txt
```
## 🗂️Each Microservice:

- Is a small standalone Python (Flask) application.
- Has its own Dockerfile to containerize it.
- Has its own requirements.txt to install dependencies.
- Returns a simple response like "User Service is running!" when accessed via a browser or API call.

All services are managed and run together using a docker-compose.yml, which:

- Builds images from the respective folders.
- Starts all services in one go.
- Exposes each service on its respective port.


## 🎯Architecture Overview (Microservices Pattern)
```

        ┌────────────┐       ┌────────────────┐
        │  Browser / │─────▶│  User Service   │ (http://localhost:5001)
        │  API Tool  │─────▶│ Product Service │ (http://localhost:5002)
        |            |     ▶│  Order Service  │ (http://localhost:5003)
        └────────────┘       └────────────────┘
```
## ⚙️ Setting Up Docker-in-Docker (DinD)

To build and run containers **from inside another container**, we used **Docker-in-Docker** (DinD) setup with --privileged mode and Docker socket mounting.

1. **Created a Docker image with Docker + Git preinstalled:**
   ```dockerfile
   FROM docker:dind
   RUN apk add --no-cache git bash
   ```

2. **Built the DinD image:**
   ```bash
   docker build -t ubuntu-dind-dev .
   ```

3. **Ran a container from this image with Docker socket sharing:**
   ```bash
   docker run -it --privileged \
     -v /var/run/docker.sock:/var/run/docker.sock \
     -v $(pwd):/workspace \
     -w /workspace \
     --name docker-dev-container \
     ubuntu-dind-dev
   ```

This enabled the container to **run Docker commands as if on the host system**.

## 🧩 What we can do with this setup:

- Learn and practice Flask microservices architecture
- Learn Docker & Docker Compose in a real-world setup
- Understand service isolation, containerization, and port mapping Extend each service to have its own:
- Database (MySQL, PostgreSQL, MongoDB, etc.)
- API endpoints (CRUD operations)
- Internal communication (via REST APIs or gRPC)

## 📌 Highlights

- Docker-in-Docker for flexible development.
- Modular microservices structure.
- Easy-to-scale containerized architecture.
- Clean CI/CD-ready setup.

## 🔮 Future Enhancements

- Add API endpoints to perform real operations like add users/products/orders.
- Connect microservices using REST calls between services.
- Add databases per service (e.g., user-db, product-db).
- Add frontend UI to consume all APIs.
- Implement service discovery, authentication, or message queues (e.g., RabbitMQ/Kafka).
- Deploy this architecture to the cloud (AWS, GCP, Azure).

## ✍️ Author

- Akhil Thyadi
- GitHub: [@akhil27051999](https://github.com/akhil27051999)

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

