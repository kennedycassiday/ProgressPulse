from django.shortcuts import render, get_object_or_404
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

def show_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list_detail": todo_list,
    }
    return render(request, "tasks/detail.html", context)
