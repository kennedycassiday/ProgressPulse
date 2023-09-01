from django.urls import path
from todos.views import (
    show_task,
    todo_list_list,
    show_todo_list,
)

urlpatterns = [
    path("tasks/", show_task),
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>", show_todo_list, name="show_todo_list"),
]
