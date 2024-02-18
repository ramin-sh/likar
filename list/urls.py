from django.urls import path
from . import views
urlpatterns = [
    path('todo', views.index, name='index'),
    path('list/', views.to_do, name='to_do'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'), 
    path('', views.login_user, name='login'),
    path('logout',views.login_user,name = 'logout'),
    path('faramooshi',views.faramooshi),
    path('setpass',views.set_pass),
    path('getmail',views.get_mail),
    path('signup/',views.signup_user, name="signup"),
]
