from django.urls import path
from todos.views import show_task

urlpatterns = [
    path("tasks/", show_task),
]
