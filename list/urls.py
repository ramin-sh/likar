from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.to_do, name='to_do'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'), 
]
