
from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("record/", views.record, name="record"),
    path("success/", views.success, name="success"),
]
