# Internship Project

## Overview

The **Internship Project** is a Django-based web application designed to manage various aspects of an internship program. It provides functionalities for handling users, tasks, and other related components, facilitating efficient management and tracking.

## Project Structure

The project is organized as follows:

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

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

* Python 3.8+
* pip
* Docker (optional, for containerized setup)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sankalp55/internship-project.git
   cd internship-project/internship_project
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   * On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

### Docker Setup (Optional)

To run the application using Docker:

1. Build the Docker image:

   ```bash
   docker build -t internship-project .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 internship-project
   ```

   The application will be accessible at `http://localhost:8000/`.

## Deployment

For deploying the application, ensure you have a platform like Heroku or Google Cloud set up. The `Procfile` and `app.yaml` are configured for such platforms.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.


## Bonus Points

* Containerize the application with Docker.
* Integrate Redis + Celery for background tasks (e.g., send a welcome email after registration).
