from django.urls import path
from todos.views import (
    show_task,
    todo_list_list,
    show_todo_list,
    create_todo_list,
    update_todo_list,
)

urlpatterns = [
    path("tasks/", show_task),
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>", show_todo_list, name="show_todo_list"),
    path("create/", create_todo_list, name="create_todo_list"),
    path("<int:id>/edit/", update_todo_list, name="update_todo_list"),
]
