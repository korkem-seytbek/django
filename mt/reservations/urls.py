from django.urls import path
from . import views

urlpatterns = [
    path("", views.reservation_list, name="reservation_list"),
    path("new/", views.reservation_create, name="reservation_create"),
    path("<int:pk>/", views.reservation_detail, name="reservation_detail"),
]

