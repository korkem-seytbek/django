from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('posts/', all_posts, name='all_posts'),
    path('posts/my', my_posts, name='my_posts'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('posts/<int:id>/delete', delete_post, name='delete_post'),
]
