from django.shortcuts import render, redirect
from app_todolist.utility import query

def view(request, id):
    post = query("SELECT * FROM todolist_post WHERE id = %s", [id])
    print(post)

    if request.method == 'POST':

        post = post[0]

        task_name = request.POST.get('task-name')
        task_desc = request.POST.get('task-desc')
        task_deadline = request.POST.get('task-deadline')

        query("UPDATE todolist_post SET task_name = %s, task_desc = %s, task_deadline = %s WHERE id = %s", [task_name,task_desc, task_deadline, id])

        return redirect("/todo/list/")

    return render(request, 'app_todolist/update.html', {'post' : post})