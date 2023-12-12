from django.urls import path
from .views import TaskListAPIView, CreateUserAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('users/', CreateUserAPIView.as_view(), name='create-user'),
]