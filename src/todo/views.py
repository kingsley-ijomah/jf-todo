from django.shortcuts import render

# Create your views here.


def list_todo(request):
    return render(request, "list_todo.html", context={})


def new_todo(request):
    return render(request, "new_todo.html", context={})


def update_todo(request, pk):
    return render(request, "update_todo.html", context={})


def delete_todo(request, pk):
    return render(request, "delete_todo.html", context={})
