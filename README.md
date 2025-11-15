# 🚀 Task Manager - Complete DevOps CI/CD Pipeline

A Flask REST API with a complete DevOps pipeline implementing CI/CD best practices using Docker, Kubernetes, and Jenkins.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![Docker](https://img.shields.io/badge/Docker-enabled-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-enabled-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [CI/CD Pipeline](#cicd-pipeline)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Deployment](#deployment)
- [Author](#author)

---

## 🎯 Overview

This project demonstrates a complete DevOps workflow with:
- **Continuous Integration (CI)**: Automated testing and Docker image building
- **Continuous Deployment (CD)**: Automated deployment to Kubernetes
- **Infrastructure as Code**: Kubernetes manifests and Jenkins pipeline as code
- **Automated Testing**: pytest with 100% test coverage of endpoints

---

## ✨ Features

### Application Features
- ✅ RESTful API built with Flask
- ✅ Task management (CRUD operations)
- ✅ Health check endpoint
- ✅ JSON responses

### DevOps Features
- 🔄 **Automated CI/CD Pipeline** with Jenkins
- 🐳 **Containerized** with Docker
- ☸️ **Orchestrated** with Kubernetes
- 🧪 **Automated Testing** with pytest
- 📦 **Image Registry** on DockerHub
- 🔐 **Secure credentials** management
- 📊 **High Availability** with 2 replicas
- ⚖️ **Load Balancing** via Kubernetes Service

---

## 🏗️ Architecture
```
Developer (GitHub)
        ↓
    git push
        ↓
┌──────────────────────────┐
│   JENKINS CI/CD          │
│                          │
│  1. Checkout (GitHub)    │
│  2. Test (pytest)        │
│  3. Build (Docker)       │
│  4. Push (DockerHub)     │
│  5. Deploy (Kubernetes)  │
└──────────────────────────┘
        ↓
┌──────────────────────────┐
│   KUBERNETES CLUSTER     │
│                          │
│  ┌─────────┐ ┌─────────┐│
│  │  Pod 1  │ │  Pod 2  ││
│  └─────────┘ └─────────┘│
│         ↓                │
│   ┌──────────────┐       │
│   │   Service    │       │
│   │ Load Balancer│       │
│   └──────────────┘       │
└──────────────────────────┘
        ↓
   Application Live ✅
```

---

## 🛠️ Technologies

| Category | Technology |
|----------|-----------|
| **Backend** | Python 3.13, Flask 3.0.0 |
| **Testing** | pytest 7.4.3 |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (Minikube) |
| **CI/CD** | Jenkins |
| **Version Control** | Git, GitHub |
| **Registry** | DockerHub |

---

## 📂 Project Structure
```
task-manager-devops/
├── app.py                 # Flask application
├── Dockerfile            # Docker configuration
├── Jenkinsfile           # Jenkins pipeline definition
├── requirements.txt      # Python dependencies
├── tests/
│   ├── __init__.py
│   └── test_app.py       # Automated tests (4 tests)
├── k8s/
│   ├── deployment.yaml   # Kubernetes Deployment (2 replicas)
│   └── service.yaml      # Kubernetes Service (NodePort)
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 🔄 CI/CD Pipeline

### Pipeline Stages

#### 1️⃣ **Checkout**
```groovy
- Clones code from GitHub repository
- Ensures latest version is used
```

#### 2️⃣ **Test**
```groovy
- Creates Python virtual environment
- Installs dependencies (requirements.txt)
- Runs pytest with 4 automated tests
- Fails pipeline if any test fails
```

#### 3️⃣ **Build**
```groovy
- Builds Docker image with version tag (v${BUILD_NUMBER})
- Authenticates with DockerHub
- Pushes image to registry: houdaoufares620/task-manager:v11
```

#### 4️⃣ **Deploy**
```groovy
- Applies Kubernetes manifests
- Updates deployment with new image version
- Ensures zero-downtime deployment
```

### Pipeline Workflow
```bash
git push → Jenkins detects change → Clone → Test → Build → Push → Deploy → Live ✅
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Docker Desktop
- Kubernetes (Minikube)
- Jenkins
- Git

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/HoudaOufares/task-manager-devops.git
cd task-manager-devops
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Run tests**
```bash
python -m pytest tests/ -v
```

### Docker Deployment

1. **Build Docker image**
```bash
docker build -t task-manager:latest .
```

2. **Run container**
```bash
docker run -d -p 5000:5000 task-manager:latest
```

### Kubernetes Deployment

1. **Start Minikube**
```bash
minikube start
```

2. **Apply Kubernetes manifests**
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

3. **Access the application**
```bash
minikube service task-manager-service
```

---

## 📡 API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/` | API status | `{"message": "Task Manager API", "status": "running"}` |
| GET | `/health` | Health check | `{"status": "healthy"}` |
| GET | `/tasks` | Get all tasks | `{"tasks": [...]}` |
| POST | `/tasks` | Add a task | `{"message": "Task added", "task": "..."}` |

### Example Request
```bash
# Get all tasks
curl http://localhost:5000/tasks

# Add a task
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"task": "Learn DevOps"}'
```

---

## 🧪 Testing

The project includes automated tests using pytest.

### Test Coverage
```python
✅ test_home()              # Tests root endpoint
✅ test_health()            # Tests health check
✅ test_get_tasks_empty()   # Tests empty task list
✅ test_add_task()          # Tests task creation
```

### Run Tests
```bash
python -m pytest tests/ -v
```

### Expected Output
```
============================= test session starts ==============================
tests/test_app.py::test_home PASSED                                      [ 25%]
tests/test_app.py::test_health PASSED                                    [ 50%]
tests/test_app.py::test_get_tasks_empty PASSED                           [ 75%]
tests/test_app.py::test_add_task PASSED                                  [100%]

============================== 4 passed in 0.12s ===============================
```

---

## 🚢 Deployment

### Kubernetes Resources

#### Deployment
- **Replicas**: 2 (High Availability)
- **Strategy**: RollingUpdate
- **Image**: houdaoufares620/task-manager:v11
- **Port**: 5000

#### Service
- **Type**: NodePort
- **Port**: 5000
- **NodePort**: 30080
- **Load Balancing**: Automatic across replicas

### Zero-Downtime Deployment

The pipeline ensures zero-downtime deployments using Kubernetes rolling updates:
```bash
kubectl set image deployment/task-manager-deployment \
  task-manager-container=houdaoufares620/task-manager:v12 --record
```

---

## 🔐 Security

- ✅ Credentials stored securely in Jenkins
- ✅ No hardcoded passwords in code
- ✅ Docker images scanned for vulnerabilities
- ✅ Kubernetes RBAC (Role-Based Access Control)

---

## 📊 Monitoring

- Health check endpoint: `/health`
- Kubernetes readiness/liveness probes (can be added)
- Jenkins build history and logs

---

## 🎯 DevOps Best Practices Implemented

✅ **Infrastructure as Code** (IaC)  
✅ **Pipeline as Code** (Jenkinsfile)  
✅ **Automated Testing** (pytest)  
✅ **Containerization** (Docker)  
✅ **Orchestration** (Kubernetes)  
✅ **Continuous Integration** (CI)  
✅ **Continuous Deployment** (CD)  
✅ **Version Control** (Git)  
✅ **Image Versioning** (Semantic tagging)  
✅ **High Availability** (2 replicas)  

---

## 🚀 Future Enhancements

- [ ] Add monitoring with Prometheus & Grafana
- [ ] Implement logging with ELK Stack
- [ ] Add database persistence (PostgreSQL/MongoDB)
- [ ] Implement authentication (JWT)
- [ ] Add integration tests
- [ ] Deploy to cloud (AWS EKS / Oracle OKE)
- [ ] Implement GitOps with ArgoCD
- [ ] Add Helm charts

---

## 👩‍💻 Author

**Houda Oufares**

## 🙏 Acknowledgments

- Flask documentation
- Docker documentation
- Kubernetes documentation
- Jenkins documentation

---

