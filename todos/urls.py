from django.urls import path
from todos.views import (
    show_task,
    todo_list_list,
)

urlpatterns = [
    path("tasks/", show_task),
    path("", todo_list_list, name="todo_list_list")
]
