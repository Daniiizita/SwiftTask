from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Task(models.Model):
    nome_usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário responsável
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WorkLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='worklogs')
    start_time = models.DateTimeField(null=True, blank=True)  # Hora de início
    end_time = models.DateTimeField(null=True, blank=True)  # Hora de fim
    duration = models.DurationField(default=timedelta)  # Duração do tempo
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            self.duration = self.end_time - self.start_time  # Calcula a duração
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.task.name} - {self.duration}"
