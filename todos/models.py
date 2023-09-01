from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    list = models.ForeignKey(
        "TodoList",
        related_name="items",
        on_delete=models.CASCADE,
    )
