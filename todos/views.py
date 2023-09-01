from django.shortcuts import render
from todos.models import TodoList

# Create your views here.


def show_task(request):
    return render(request, "tasks/detail.html")

def todo_list_list(request):
    todos = TodoList.objects.all
    context = {
        "todo_list_list": todos,
    }
    return render(request, "tasks/list.html", context)
