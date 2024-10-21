from django.urls import path
from .views import TaskCreateView, WorkLogCreateView

urlpatterns = [
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('worklog/create/', WorkLogCreateView.as_view(), name='worklog_create'),
]
