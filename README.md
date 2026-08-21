# Django Blog API

A multi-app REST API for a blogging platform, built with Django REST Framework, JWT authentication, and PostgreSQL.

## Apps
- accounts: user profiles and registration
- posts: categories, tags, posts (with likes, bookmarks, view counts, read time, excerpts)
- comments: post comments

## Features
- JWT authentication (login, token refresh)
- Public registration for regular (non-admin) users
- Full CRUD on posts, categories, tags, comments
- Like and bookmark toggle actions
- Homepage, author profile, search, and trending endpoints
- Auto-generated slugs and excerpts
- View count tracking

## Tech Stack
- Python / Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- django-cors-headers

## Setup
1. Create a virtual environment: python3 -m venv venv && source venv/bin/activate
2. Install dependencies: pip install -r requirements.txt
3. Create a PostgreSQL database and a .env file with DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
4. Run migrations: python manage.py migrate
5. Create a superuser: python manage.py createsuperuser
6. Start the server: python manage.py runserver

## Key Endpoints
- POST /api/register/ — register a new user
- POST /api/token/ — obtain JWT tokens
- GET /api/posts/ — list posts
- POST /api/posts/<id>/like/ — toggle like
- POST /api/posts/<id>/bookmark/ — toggle bookmark
- GET /api/home/ — recent published posts
- GET /api/trending/ — posts sorted by views
- GET /api/search/?q=... — search posts
- GET /api/authors/<username>/ — author profile and their posts
