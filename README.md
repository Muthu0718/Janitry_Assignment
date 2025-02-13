Janitri Backend API
This project provides a RESTful API to manage users, patients, and heart rate data. The backend is developed using Django and Django Rest Framework (DRF). This API can be used for managing healthcare-related data, including user authentication, patient records, and heart rate tracking.

Table of Contents
Project Setup
Assumptions & Decisions
API Documentation
Running the Server
Testing the API
Future Improvements
Project Setup
Follow the instructions below to set up and run the project locally.

1. Clone the Repository
bash
Copy
git clone https://github.com/yourusername/janitri_backend.git
cd janitri_backend
2. Set Up a Virtual Environment
For Windows:
bash
Copy
python -m venv venv
.\venv\Scripts\activate
For macOS/Linux:
bash
Copy
python3 -m venv venv
source venv/bin/activate
3. Install Required Dependencies
Install the required dependencies listed in requirements.txt. If requirements.txt is missing, you can manually install the dependencies:

bash
Copy
pip install django djangorestframework psycopg2
Note: If you are using PostgreSQL, ensure that psycopg2 is installed. If you plan to use SQLite, the default database setup will work without any additional setup.

4. Database Setup
In janitri_backend/settings.py, configure your database. By default, Django uses SQLite for local development. To use PostgreSQL, you need to configure the database settings as follows:
python
Copy
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'janitri_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Create the database and run migrations:
bash
Copy
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser (Optional)
To access the Django admin interface, create a superuser:

bash
Copy
python manage.py createsuperuser
Assumptions & Decisions
Assumptions
Authentication: No complex authentication system (like JWT) is set up in this project. User login is done by matching email and password directly.
Database: The project is set to use SQLite by default, suitable for development. For production, it's recommended to use PostgreSQL.
Password Management: For simplicity, passwords are stored in plain text, but in production, password hashing should be used (Django handles this automatically with its User model).
Decisions
No Token-based Authentication: Since this is a basic project, token-based authentication (e.g., JWT) is not implemented. A more secure approach would involve implementing this in the future.
Date Handling: We are using ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ) for all date/time fields to ensure consistency and ease of use with front-end or other systems consuming this API.
User Management: We extend Django's built-in user model minimally, focusing on email and password. You can later add additional fields such as first_name, last_name, etc.
API Documentation
The project exposes the following endpoints:

1. User Registration
URL: /api/users/register/
Method: POST
Request Body:
json
Copy
{
    "email": "user@example.com",
    "password": "password123"
}
Response:
json
Copy
{
    "id": 1,
    "email": "user@example.com",
    "password": "password123"
}
2. User Login
URL: /api/users/login/
Method: POST
Request Body:
json
Copy
{
    "email": "user@example.com",
    "password": "password123"
}
Response:
json
Copy
{
    "message": "Login successful",
    "user": {
        "id": 1,
        "email": "user@example.com"
    }
}
3. Add Patient
URL: /api/patients/
Method: POST
Request Body:
json
Copy
{
    "name": "John Doe",
    "age": 30,
    "date_of_birth": "1995-03-25T10:30:00Z",
    "user": 1
}
Response:
json
Copy
{
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "date_of_birth": "1995-03-25T10:30:00Z",
    "user": 1
}
4. Get Patients of a User
URL: /api/patients/<user_id>/
Method: GET
Response:
json
Copy
[
    {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "date_of_birth": "1995-03-25T10:30:00Z",
        "user": 1
    }
]
5. Record Heart Rate
URL: /api/heart_rates/
Method: POST
Request Body:
json
Copy
{
    "rate": 72,
    "timestamp": "2025-02-13T10:00:00Z",
    "patient": 1
}
Response:
json
Copy
{
    "id": 1,
    "rate": 72,
    "timestamp": "2025-02-13T10:00:00Z",
    "patient": 1
}
6. Get Heart Rates of a Patient
URL: /api/heart_rates/<patient_id>/
Method: GET
Response:
json
Copy
[
    {
        "id": 1,
        "rate": 72,
        "timestamp": "2025-02-13T10:00:00Z",
        "patient": 1
    }
]
Running the Server
To run the Django development server, use the following command:

bash
Copy
python manage.py runserver
The server will be running at http://127.0.0.1:8000/. You can use Postman, cURL, or your browser to interact with the API.

Testing the API
You can test the API using Postman or cURL:

Using Postman
Import the provided Postman collection or manually create requests with the endpoints described above.
Set the request type (POST/GET) and the request body (for POST requests).
Using cURL
You can use the following curl command to test the User Registration API:

bash
Copy
curl -X POST http://127.0.0.1:8000/api/users/register/ \
-H "Content-Type: application/json" \
-d '{"email": "user@example.com", "password": "password123"}'
Future Improvements
Authentication: Implement a more secure authentication system using Django Rest Framework's token-based authentication (or JWT).
Password Security: Hash passwords using Django's make_password() for security.
Unit Tests: Add tests to ensure the correctness and reliability of the API.
Permissions & Roles: Implement permissions and role-based access control, such as ensuring users can only modify their own data.
Admin Panel: Create a custom admin panel to manage users, patients, and heart rates via the web interface.
Additional Notes
Date & Time: All date fields are expected to follow the ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ), which is widely accepted for APIs.
Handling Errors: Ensure proper error handling (e.g., for invalid user input or missing fields) in production environments.
Production Deployment: For production deployment, ensure to configure settings for security, performance, and database optimizations.
This should serve as a solid foundation to help you understand, run, and test the Django-based backend API for your project!
