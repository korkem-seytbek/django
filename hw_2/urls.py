from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ панеліне кіретін сілтеме
    path('', include('movie.urls')),  # Movie қосымшасының URL сілтемесі
    path('', include('blog.urls')),   # Blog қосымшасының URL сілтемесі
]
