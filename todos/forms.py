from django.forms import ModelForm
from todos.models import TodoList, TodoItem

class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "name",
        ]

class ItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = "__all__"
