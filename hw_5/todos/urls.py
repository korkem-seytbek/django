from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Добавляем маршрут для главной страницы
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/new/', views.todo_create, name='todo_create'),
    path('todos/<int:id>/delete/', views.todo_delete, name='todo_delete'),
    path('profile/', views.profile, name='profile'), 
    
]
