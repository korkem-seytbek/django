from django.urls import path
from . import views

urlpatterns = [
    path("", views.table_list, name="table_list"),
    path("new/", views.table_create, name="table_create"),
    path("available/", views.table_available, name="table_available"),
]

