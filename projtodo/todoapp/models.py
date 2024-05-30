from django.db import models

# Create your models here.
class ToDoList(models.Model):
    Title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Title