from django.shortcuts import render
from .models import MyTasks
# Create your views here.
def task(request):
    task = MyTasks.objects.order_by('-task_name')
    return render(request, 'todolist/task.html',{'task':task})