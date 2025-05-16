from django.shortcuts import render, redirect
from app_todolist.utility import query

def view(request, id):
    if request.method == 'GET':
        post = query("DELETE FROM todolist_post WHERE id = %s", [id])
        print(post)

    return redirect("/todo/list/", name="list")