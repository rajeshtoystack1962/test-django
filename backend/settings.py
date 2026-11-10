"""Minimal Django settings. No database. The React app is allowed to call this API."""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-insecure-change-me")
DEBUG = os.environ.get("DJANGO_DEBUG", "true").lower() == "true"
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",")
    if host.strip()
]

INSTALLED_APPS = [
    "corsheaders",
    "api.apps.ApiConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "backend.urls"
WSGI_APPLICATION = "backend.wsgi.application"

# Items live in memory inside api/views.py. Nothing is saved to disk.
DATABASES = {}

# Browsers block a page on port 5173 or 3000 from calling port 8000
# unless this API lists those pages here. The React dev server and
# server.js avoid that by forwarding /api themselves. These origins
# still matter if the browser calls Django directly.
def _origins(value):
    origins = []
    for part in value.split(","):
        origin = part.strip().rstrip("/")
        if origin:
            origins.append(origin)
    return origins


CORS_ALLOWED_ORIGINS = _origins(
    os.environ.get(
        "CORS_ALLOWED_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000,http://127.0.0.1:3000",
    )
)

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_TZ = True
