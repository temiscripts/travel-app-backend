# This document serves as the official guide for setting up and understanding the foundational architecture of the Travel Application Backend.

## 🎯 Project Overview

The **Travel Application** is a dynamic web application backend built using **Django** and the **Django REST Framework (DRF)**. This project focuses on establishing a professional, production-ready foundation, integrating secure configuration practices, robust database management with MySQL, and key DevOps tooling for future scalability.

## ⚙️ Technologies & Dependencies

| Category | Tool/Package | Professional Purpose |
| :--- | :--- | :--- |
| **Framework** | Django, DRF | Core components for building robust, scalable APIs. |
| **Security** | `django-environ` | Manages environment variables for secure configuration (secrets management). |
| **Documentation** | `drf-yasg` (Swagger) | Automatically generates interactive API documentation from the code. |
| **Database** | MySQL, `mysqlclient` | Relational database chosen for high performance and data integrity. |
| **Asynchronous** | `celery`, `rabbitmq` | Installed for future offloading of long-running tasks. |
| **CORS** | `django-cors-headers` | Enables secure communication between the API and a separate frontend client. |

***

## 🚀 Getting Started (Windows Setup)

### 1. Prerequisites

* **Python 3.x** installed.
* **MySQL Server** installed and running locally (default port: 3306).
* A dedicated, empty **MySQL database** created for the project (e.g., travel_db`).

### 2. Environment and Dependencies

Execute these commands in your **PowerShell terminal** while in the project root:

```powershell
# Ensure you are in the project root folder (containing manage.py)

# 1. Create the virtual environment folder
py -3 -m venv .venv

# 2. Activate the environment (The prompt will change to include '(.venv)')
.\.venv\Scripts\activate

# 3. Install all packages listed in requirements.txt
pip install -r requirements.txt
```

### 3. Secure Configuration (.env File)

Create a file named .env in the project root. REMINDER: This file must be in your .gitignore to prevent committing secrets.

```dotenv
# .env file (DO NOT COMMIT THIS FILE)

# 1. Security & Environment
SECRET_KEY='[A_LONG_RANDOM_SECRET_KEY]'
DEBUG=True
ALLOWED_HOSTS='localhost,127.0.0.1'

# 2. Database (MySQL credentials)
DB_ENGINE='django.db.backends.mysql'
DB_NAME='travel_db' 
DB_USER='root'
DB_PASSWORD='YOUR_MYSQL_ROOT_PASSWORD'
DB_HOST='localhost'
DB_PORT='3306'

# 3. Asynchronous Broker (RabbitMQ Default)
CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
CELERY_RESULT_BACKEND=redis://localhost:6379/0 
```

### 4. Database Initialization
Run migrations to apply the default Django schema (users, admin, etc.) to your configured MySQL database:

```powerShell
(.venv) PS> python manage.py migrate
```

### 5 Running the Server
Start the development server:
```powershell
(.venv) PS> python manage.py runserver
```
🌐 API Documentation and Access

After completing the setup and running the development server:

Start the server:
(.venv) PS> python manage.py runserver

Access Interactive Documentation (Swagger UI):
Open your browser and navigate to:
👉 http://127.0.0.1:8000/swagger/