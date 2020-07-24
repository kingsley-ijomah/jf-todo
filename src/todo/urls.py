from django.urls import path

from .views import delete_todo, list_todo, new_todo, update_todo

app_name = "todo"

urlpatterns = [
    path("", list_todo, name="list-todo"),
    path("new-todo", new_todo, name="new-todo"),
    path("update-todo/<int:pk>", update_todo, name="update-todo"),
    path("delete-todo/<int:pk>", delete_todo, name="delete-todo"),
]
