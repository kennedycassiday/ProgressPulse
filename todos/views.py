from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoForm, ItemForm

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

def create_todo_list(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("show_todo_list", id=list.id)
    else:
        form = TodoForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)

def update_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo_list)
        if form.is_valid():
            list = form.save()
            return redirect("show_todo_list", id=list.id)
    else:
        form = TodoForm(instance=todo_list)

    context = {
        "todo_list_detail": todo_list,
        "form": form,
    }
    return render(request, "tasks/edit.html", context)

def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        todo_list.delete()
        return redirect("todo_list_list")
    return render(request, "tasks/delete.html")

def create_todo_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("show_todo_list", id=item.list.id)
    else:
        form = ItemForm()
        context = {
            "form": form
        }
        return render(request, "tasks/create_item.html", context)

def update_todo_item(request, id):
    item = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect("show_todo_list", id = item.list.id)
    else:
        form = ItemForm(instance=item)
        context = {
            "form": form
        }
        return render(request, "tasks/edit_item.html/", context)
