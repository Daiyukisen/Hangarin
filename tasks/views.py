from django.shortcuts import render
from .models import Task

def task_list(request):
    # Fetch all tasks and include related category and priority for the dashboard
    tasks = Task.objects.select_related('category', 'priority').all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})