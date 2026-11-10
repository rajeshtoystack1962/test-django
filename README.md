# django-backend

Small Django API for learning. It has **no database**. Items are stored in memory and reset when the process stops.

The React app in `../react-frontend` calls this API. Keep both folders as neighbors.

## What the frontend calls

| Method | URL | Description |
|---|---|---|
| GET | `/api/health/` | Health check |
| GET | `/api/message/` | Hello message, hostname, and time |
| GET | `/api/items/` | List items |
| POST | `/api/items/` | Add an item. Body: `{"name": "My item"}` |

## How the two apps are connected

The browser page runs on another port (5173 while learning, 3000 for a local deploy). Django lists those pages in `CORS_ALLOWED_ORIGINS` inside `.env`, so a browser is allowed to call this API.

For the normal local setup you do **not** need the browser to call port 8000 itself. The React app receives `/api/...` and forwards it here. `BACKEND_URL` in the frontend `.env` is the address of this server: `http://localhost:8000`.

## Run it (do this first)

```bash
cd django-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

`.env` is already filled in for localhost. To change it later, edit `.env` (copy from `.env.example` if you lost it) and start the server again.

Check:

```bash
curl http://localhost:8000/api/message/
```

Leave this terminal running, then start the React app. See `../react-frontend/README.md`.

## Environment variables

| Variable | Default | Meaning |
|---|---|---|
| `DJANGO_SECRET_KEY` | dev key | Change this on a real server |
| `DJANGO_DEBUG` | `true` | Error details on or off |
| `DJANGO_ALLOWED_HOSTS` | `*` | Hostnames Django accepts |
| `CORS_ALLOWED_ORIGINS` | frontend on ports 5173 and 3000 | Pages allowed to call this API from the browser |

## Optional: run it like a small server

With the virtualenv activated:

```bash
gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 2
```
