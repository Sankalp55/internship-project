# Internship Project

A Django web application for internship with simple user, task, and notification management.

<p align="center">
  <img alt="Django" src="https://img.shields.io/badge/Django-Framework-informational">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-blue">
  
</p>

## Overview

This project provides a clean starting point for an management portal.  
It includes:

- **Users app** for authentication and profile handling  
- **Tasks app** for assigning and tracking tasks  
- **Notifications app** for system messages and alerts  
- **Home app** for basic landing and static pages  

The setup supports local development and containerized runs with Docker.

## Project structure

```
internship_project/
├── home/
├── internship_project/        # Django settings, URLs, ASGI/WSGI
├── notifications/             # Notifications system
├── tasks/
├── users/
├── app.yaml                   # Example App Engine config
├── db.sqlite3                 # Local dev database
├── docker-compose.yml
├── Dockerfile
├── .dockerignore
├── manage.py
├── Procfile                   # Example Heroku process definition
└── requirements.txt
```

## Requirements

- Python 3.8 or newer  
- pip  
- Optional: Docker Desktop for container runs  

## Quick start

Clone the repository and move into the project folder:

```bash
git clone https://github.com/Sankalp55/internship-project.git
cd internship-project/internship_project
```

Create a virtual environment and activate it:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS or Linux
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations and create an admin user:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Now open http://127.0.0.1:8000

## Environment variables

Create a `.env` file or use your shell to set variables. Common ones:

```
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

If you later switch from SQLite to another database, add something like:

```
DATABASE_URL=postgres://user:pass@host:5432/dbname
```

If you enable a task queue, you may also use:

```
REDIS_URL=redis://localhost:6379/0
```

## API usage

By default the API is served under:

```
Base URL: http://127.0.0.1:8000/api/
```

### Users

```
GET    /api/users/           List users
POST   /api/users/           Create user
GET    /api/users/<id>/      Retrieve user
PUT    /api/users/<id>/      Update user
DELETE /api/users/<id>/      Delete user
```

### Tasks

```
GET    /api/tasks/           List tasks
POST   /api/tasks/           Create task
GET    /api/tasks/<id>/      Retrieve task
PUT    /api/tasks/<id>/      Update task
DELETE /api/tasks/<id>/      Delete task
```

### Notifications

```
GET    /api/notifications/           List notifications
POST   /api/notifications/           Create notification
GET    /api/notifications/<id>/      Retrieve notification
PUT    /api/notifications/<id>/      Update notification
DELETE /api/notifications/<id>/      Delete notification
```

Example requests:

```bash
# Create a user
curl -X POST http://127.0.0.1:8000/api/users/   -H "Content-Type: application/json"   -d '{"username":"john","email":"john@example.com"}'

# List tasks
curl http://127.0.0.1:8000/api/tasks/

# List notifications
curl http://127.0.0.1:8000/api/notifications/
```

## Running with Docker

Build and run the app in a container:

```bash
# From the internship_project directory
docker build -t internship-project .
docker run -p 8000:8000 internship-project
```

Or use `docker-compose` if the file is configured for your environment:

```bash
docker compose up --build
```

## Optional background tasks

If the project includes Celery and Redis in `requirements.txt` and settings, you can run a worker locally like this:

```bash
# Start Redis (for example with Docker)
docker run -p 6379:6379 redis:alpine

# In another terminal, from the internship_project directory
celery -A internship_project worker -l info
```

If you do not see Celery configuration in `settings.py` or a `celery.py` in the Django project, you can ignore this section.

## Admin access

Visit:

```
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials you created.

## Tests

If tests are added, you can run them with:

```bash
python manage.py test
```

## Contributing

1. Create a feature branch  
2. Commit changes with clear messages  
3. Open a pull request for review  


