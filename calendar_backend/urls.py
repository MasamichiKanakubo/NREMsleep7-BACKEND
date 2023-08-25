from django.urls import path
from calendar_backend import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
