# Task Management API Documentation

This API allows you to perform CRUD operations on tasks. It is built using Django Rest Framework and includes authentication, permissions, and unit tests.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/task-management-api.git
   cd task-management-api


-->Install dependencies:
        pip install -r requirements.txt

-->Apply migrations:
        python manage.py migrate

-->Create a superuser for authentication:
        python manage.py createsuperuser

-->Run the development server:
        python manage.py runserver

        -->The API will be available at http://127.0.0.1:8000/api/tasks/

#Authentication:
Token-based authentication is used for the API. To authenticate, include the token in the Authorization header of your requests:

        Authorization: Token your_token_here

    	
Endpoints:
    -->List all tasks
        URL: /api/tasks/
        Method: GET
        Authentication: Required

    -->Retrieve a single task by ID
        URL: /api/tasks/<task_id>/
        Method: GET
        Authentication: Required

    -->Create a new task
        URL: /api/tasks/
        Method: POST
        Authentication: Required
        Data:
            {
                "title": "Task Title",
                "description": "Task Description",
                "due_date": "YYYY-MM-DD",
                "status": "Pending"
            }

    -->Update an existing task
        URL: /api/tasks/<task_id>/
        Method: PUT
        Authentication: Required
        Data:
            {
                "title": "Updated Task Title",
                "description": "Updated Task Description",
                "due_date": "YYYY-MM-DD",
                 "status": "Completed"
            }

    -->Delete a task
        URL: /api/tasks/<task_id>/
        Method: DELETE
        Authentication: Required

    Permissions
        Only authenticated users can perform CRUD operations.
        Users can only update or delete tasks that they own.

    Unit Tests
        Run unit tests using:
                python manage.py test
