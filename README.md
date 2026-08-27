# Library — Books API

A RESTful **Books API** built with **Django** and **Django REST Framework (DRF)**, featuring user authentication via **dj-rest-auth** / **django-allauth**, and interactive API documentation via **drf-yasg** (Swagger / ReDoc, OpenAPI 2.0).

## Features

- Full CRUD for books (list, create, retrieve, update, partial update, delete) via a DRF `ModelViewSet` + router
- Custom validation on book creation (alphabetic titles, duplicate title+author check, price range check)
- Authentication endpoints powered by `dj-rest-auth` and `django-allauth`:
  - Login / Logout
  - Registration with email verification
  - Password change and password reset (with email confirmation)
  - Retrieve/update current user details
- Interactive Swagger UI and ReDoc documentation
- Django admin panel

## Tech Stack

- Python 3.14
- Django
- Django REST Framework
- drf-yasg (OpenAPI/Swagger docs)
- dj-rest-auth + django-allauth (authentication)
- SQLite (default dev database)
- Pipenv (dependency management)

## Project Structure

```
Library/
├── books/                  # Books app
│   ├── models.py           # Book model
│   ├── serializers.py      # BookSerializer with custom validation
│   ├── views.py            # BookViewSet (ModelViewSet) + router
│   ├── urls.py
│   └── migrations/
├── library_project/         # Project config
│   ├── settings.py
│   ├── urls.py              # Root URLs, Swagger/ReDoc schema
│   ├── wsgi.py / asgi.py
├── manage.py
├── Pipfile
└── Pipfile.lock
```

## Book Model

| Field    | Type          | Notes                          |
|----------|---------------|---------------------------------|
| title    | CharField     | max length 200                  |
| subtitle | CharField     | max length 200                  |
| content  | TextField     |                                  |
| author   | CharField     | max length 100                  |
| isbn     | CharField     | max length 13                   |
| price    | DecimalField  | max digits 20, 2 decimal places; must be between 0 and 999999 |

## Getting Started

### Prerequisites

- Python 3.14
- [Pipenv](https://pipenv.pypa.io/) installed (`pip install pipenv`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/davlatbekzoirov/Library.git
   cd Library
   ```

2. Install dependencies with Pipenv:
   ```bash
   pipenv install
   pipenv shell
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/api/v1/`.

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`
- Django admin: `http://127.0.0.1:8000/admin/`

## API Endpoints

### Books (`/api/v1/books/`)

| Method | Endpoint              | Description             |
|--------|------------------------|--------------------------|
| GET    | `/api/v1/books/`      | List all books           |
| POST   | `/api/v1/books/`      | Create a new book        |
| GET    | `/api/v1/books/{id}/` | Retrieve a single book   |
| PUT    | `/api/v1/books/{id}/` | Update a book (full)     |
| PATCH  | `/api/v1/books/{id}/` | Update a book (partial)  |
| DELETE | `/api/v1/books/{id}/` | Delete a book             |

### Authentication (`/api/v1/dj-rest-auth/`)

| Method        | Endpoint                                          | Description                                        |
|---------------|------------------------------------------------------|-------------------------------------------------------|
| POST          | `/dj-rest-auth/login/`                             | Log in                                                |
| GET/POST      | `/dj-rest-auth/logout/`                            | Log out                                               |
| POST          | `/dj-rest-auth/password/change/`                   | Change the current user's password                    |
| POST          | `/dj-rest-auth/password/reset/`                    | Request a password reset email                        |
| POST          | `/dj-rest-auth/password/reset/confirm/`            | Confirm password reset via emailed link                |
| POST          | `/dj-rest-auth/registration/`                      | Register a new user                                    |
| POST          | `/dj-rest-auth/registration/resend-email/`         | Resend verification email                             |
| POST          | `/dj-rest-auth/registration/verify-email/`         | Verify email using the provided key                    |
| GET/PUT/PATCH | `/dj-rest-auth/user/`                              | Retrieve or update current user's details              |

### Other

| Method | Endpoint     | Description                    |
|--------|--------------|----------------------------------|
| GET    | `/api-auth/` | DRF's browsable-API login/logout |

## Authentication Notes

By default, this project uses DRF's `SessionAuthentication` and `BasicAuthentication` classes, and all endpoints require authentication (`IsAuthenticated` is the default permission class). To authenticate:

- Log in via the browsable API at `/api-auth/login/`, **or**
- Send credentials via HTTP Basic Auth, **or**
- Use the `/api/v1/dj-rest-auth/login/` endpoint.

> Note: `rest_framework.authtoken` is installed, but the `REST_FRAMEWORK` settings currently do not include `TokenAuthentication` in `DEFAULT_AUTHENTICATION_CLASSES`. Add it to `settings.py` if you want to authenticate using auth tokens returned by dj-rest-auth's login endpoint.

## Email

Emails (e.g. registration verification, password reset) are sent to the console during development:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Update this in `library_project/settings.py` to a real backend (e.g. SMTP) for production use.

## Development Notes

- `DEBUG = True` and a hardcoded `SECRET_KEY` are set for local development only — **do not use these settings in production**.
- The database is SQLite (`db.sqlite3`) by default; swap in PostgreSQL/MySQL for production via the `DATABASES` setting.
