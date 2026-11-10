from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health),
    path("message/", views.message),
    path("items/", views.items),
]
