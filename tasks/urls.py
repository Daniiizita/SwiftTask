from django.urls import path
from .views import TaskCreateView, WorkLogCreateView, start_worklog, stop_worklog, TaskListView

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('worklog/create/', WorkLogCreateView.as_view(), name='worklog_create'),
    path('start/<int:task_id>/', start_worklog, name='start_worklog'),
    path('stop/<int:worklog_id>/', stop_worklog, name='stop_worklog'),
    path('', TaskListView.as_view(), name='task_list'),  # Definindo a lista de tarefas
]