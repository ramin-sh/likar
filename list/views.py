from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    todo_items = Todo.objects.all().order_by()
    return render(request, "list/index.html" , {"todo_items": todo_items})
    
def to_do(request):
    current_date = timezone.now()
    content = request.POST.get('content')
    Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
