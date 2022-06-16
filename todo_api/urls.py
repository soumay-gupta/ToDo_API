from django.urls import include, re_path as url
from django.urls import path, include

from .views import (
    TodoListApiView,
    TodoListApiView
)

urlpatterns = [
    path('todo_api', TodoListApiView.as_view()),
    path('todo_api/<int:todo_id>/', TodoListApiView.as_view()),
]