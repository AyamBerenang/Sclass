from django.shortcuts import render
from app_todolist.utility import query

def view(request):
    if request.method == 'POST':
        task_name = request.POST.get('task-name')
        task_desc = request.POST.get('task-desc')
        task_deadline = request.POST.get('task-deadline')

        result = query("INSERT INTO todolist_post (task_name, task_desc, task_deadline) VALUES (%s, %s, %s)", [task_name,task_desc, task_deadline])
        print(result)

    return render(request, 'app_todolist/create.html')