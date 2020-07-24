from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoForm
from .models import Todo

# FBV (funcion based views)


def list_todo(request):
    todos = Todo.objects.all()
    return render(request, "list_todo.html", context={"todos": todos})


def new_todo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("todo:list-todo")

    return render(request, "new_todo.html", context={"form": form})


def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        form.save()
        return redirect("todo:list-todo")

    return render(request, "update_todo.html", context={"form": form})


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        todo.delete()
        return redirect("todo:list-todo")

    return render(request, "delete_todo.html", context={})
