from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, WorkLog

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    # Definimos o usuário logado como responsável pela tarefa
    def form_valid(self, form):
        form.instance.nome_usuario = self.request.user  # Adiciona o usuário logado como responsável
        return super().form_valid(form)

class WorkLogCreateView(LoginRequiredMixin, CreateView):
    model = WorkLog
    fields = ['task', 'date', 'time_spent', 'description']
    template_name = 'tasks/worklog_form.html'
    success_url = reverse_lazy('worklog_list')

    # Filtramos as tarefas para exibir apenas as pertencentes ao usuário logado
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['task'].queryset = Task.objects.filter(nome_usuario=self.request.user)
        return form

    