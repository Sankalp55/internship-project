# Internship Project

## Overview

The **Internship Project** is a Django-based web application designed to manage various aspects of an internship program. It provides functionalities for handling users, tasks, and other related components, facilitating efficient management and tracking.

## Project Structure

```
internship_project/
├── home/
├── internship_project/
├── tasks/
├── users/
├── app.yaml
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── .dockerignore
├── manage.py
├── Procfile
└── requirements.txt
```

* **home/**: Contains views and templates related to the homepage.
* **internship\_project/**: Core project settings and configurations.
* **tasks/**: Manages task-related functionalities.
* **users/**: Handles user authentication and profiles.
* **app.yaml**: Configuration file for deployment platforms like Google Cloud.
* **db.sqlite3**: SQLite database file.
* **docker-compose.yml**: Defines services for Docker containers.
* **Dockerfile**: Instructions for building the Docker image.
* **.dockerignore**: Specifies files to be ignored by Docker.
* **manage.py**: Command-line utility for administrative tasks.
* **Procfile**: Specifies commands for deploying on platforms like Heroku.
* **requirements.txt**: Lists Python dependencies.

## Project Setup Instructions

### Prerequisites

* Python 3.8+
* pip
* Docker (optional)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Sankalp55/internship-project.git
cd internship-project/internship_project
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create superuser:

```bash
python manage.py createsuperuser
```

6. Run server:

```bash
python manage.py runserver
```

Access at `http://127.0.0.1:8000/`.

### Docker Setup (Optional)

```bash
docker build -t internship-project .
docker run -p 8000:8000 internship-project
```

## API Usage Guide

### Base URL

```
http://127.0.0.1:8000/api/
```

### Endpoints

* **Users**

  * `GET /api/users/` - List all users
  * `POST /api/users/` - Create a new user
  * `GET /api/users/<id>/` - Get user details
  * `PUT /api/users/<id>/` - Update user
  * `DELETE /api/users/<id>/` - Delete user

* **Tasks**

  * `GET /api/tasks/` - List all tasks
  * `POST /api/tasks/` - Create a task
  * `GET /api/tasks/<id>/` - Get task details
  * `PUT /api/tasks/<id>/` - Update task
  * `DELETE /api/tasks/<id>/` - Delete task

### Sample Requests

```bash
# Create user
curl -X POST http://127.0.0.1:8000/api/users/ -H "Content-Type: application/json" -d '{"username":"john","email":"john@example.com"}'

# Get tasks
curl http://127.0.0.1:8000/api/tasks/
```

## Bonus Tasks Completed

* Containerized the application using Docker.
* Integrated Redis + Celery for background tasks (e.g., sending a welcome email after registration).
