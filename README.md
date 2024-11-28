# color-palette
color-palette

# Prerequisites
It is easy to run with docker compose.
Other wise you need to have
- Python 3.12
- pipenv
- Node.js
- npm
- make (optional, there are some make commands)

Create .env file in the root directory and add the following variables:
```
echo "DJANGO_SECRET_KEY=your_secret_key" >> .env
echo "DJANGO_DEBUG=True" >> .env
echo "DJANGO_LOG_LEVEL=DEBUG=DEBUG" >> .env
echo "DJANGO_ALLOWED_HOSTS=localhost" >> .env
echo "DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:8000" >> .env
echo "DJANGO_CORS_ALLOWED_ORIGINS=http://localhost:3000" >> .env
```
# Run
```
docker compose up
```

# Frontend
Frontend is built with React. It is served on http://localhost:3000
It will show 5 lines of color palettes. You can click to regenerate the colors.

To start the frontend in development mode:
```
cd frontend
npm install
npm start
```

# Backend
Backend is built with Django. It is served on http://localhost:8000
It has a single endpoint to generate random color palettes.

To start the backend in development mode:
```
cd backend
cp .env.example .env
pipenv install
pipenv run python manage.py runserver
```
