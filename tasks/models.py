from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    nome_usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name

class WorkLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE) 
    date = models.DateField() 
    time_spent = models.DecimalField(max_digits=5, decimal_places=2) 
    description = models.TextField()  

    def __str__(self):
        return f"{self.task.name} - {self.date}"
