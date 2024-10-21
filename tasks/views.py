from django.shortcuts import render, get_object_or_404, redirect 
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, WorkLog
from django.contrib import messages
from django.utils.timezone import now
from django.views.generic.list import ListView
from .models import Task

def index(request):
    return render(request, 'index.html')

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    # Definimos o usuário logado como responsável pela tarefa
    def form_valid(self, form):
        form.instance.nome_usuario = self.request.user
        return super().form_valid(form)

class WorkLogCreateView(LoginRequiredMixin, CreateView):
    model = WorkLog
    fields = ['task', 'start_time', 'end_time', 'description']  # Campos existentes no modelo
    template_name = 'worklog_form.html'
    success_url = reverse_lazy('worklog_list')

    # Filtramos as tarefas para exibir apenas as pertencentes ao usuário logado
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['task'].queryset = Task.objects.filter(nome_usuario=self.request.user)
        return form

def start_worklog(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    worklog = WorkLog.objects.create(task=task, start_time=now())
    messages.success(request, f"Início da tarefa '{task.name}' registrado.")
    return redirect(reverse('worklog_list'))  # Redireciona para a lista de worklogs

def stop_worklog(request, worklog_id):
    worklog = get_object_or_404(WorkLog, id=worklog_id, end_time__isnull=True)
    worklog.end_time = now()
    worklog.save()
    messages.success(request, f"Término da tarefa '{worklog.task.name}' registrado.")
    return redirect(reverse('task_list'))  # Redireciona para a lista de tarefas

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tarefas'


