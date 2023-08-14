from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list),
    path("todos/<int:pk>", views.todo_detail),
]