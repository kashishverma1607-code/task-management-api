# Task Management API

A simple REST API built with Python and FastAPI to manage tasks. It supports creating, viewing, updating, and deleting tasks.

## Features

- Create a new task
- View all tasks
- View a task by ID
- Update task details and completion status
- Delete a task
- Handle errors for tasks that do not exist
- Automated API tests using Pytest

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pytest
- HTTPX

## Project Structure

```text
task-management-api/
├── app/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd task-management-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Install dependencies:

```bash
venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run the API

```bash
venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Open the interactive API documentation in your browser:

http://127.0.0.1:8000/docs

## Run Tests

```bash
venv\Scripts\python.exe -m pytest tests -v
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a task |
| GET | `/tasks/{task_id}` | Get a task by ID |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Learning Outcomes

- Building REST APIs with FastAPI
- Working with HTTP methods and status codes
- Handling API errors
- Writing automated tests with Pytest

## Author

Kashish Verma
