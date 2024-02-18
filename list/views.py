from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .froms import *
import random
# Create your views here.
def generate_random_code():
    code = random.randint(100000, 999999)
    return code
random_code = str(generate_random_code())


def index(request):
    u = User.objects.get(username = request.user)
    todo_items = Todo.objects.filter(person=u).order_by()
    return render(request, "list/index.html" , {"todo_items": todo_items})
    
def to_do(request):
    current_date = timezone.now()
    content = request.POST.get('content')
    print(request.user)
    u = User.objects.get(username = request.user)
    Todo.objects.create(added_date=current_date, text=content,person=u)
    return HttpResponseRedirect("/todo")

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/todo")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"با موفقیت وارد شدید")
            return redirect("index")
        else:
            messages.success(request,"نام کاربری یا کلمه عبور اشتباه است")
            return redirect("login")
    
    return render(request,'list/login.html')


def logout_user(request):
    logout(request)
    messages.success(request,"با موفقیت خارج شدید")
    return redirect("login")


def faramooshi(request):

    

    #send_mail('safafromdjango','from django',settings.EMAIL_HOST_USER,['your mail'])
    #User.objects.get()
    

    if request.method == 'GET':
        
        return render(request,"resetpassword/code.html")
        
    else:
        if request.POST.get('code') == random_code:
            
            return render(request,'resetpassword/passwordset.html')
            
        else:
            return HttpResponse('کد وارد شده صحیح نمی باشد')
    #---------------------


def set_pass(request):
    if request.method == 'POST':
        user_password = request.POST.get('pass')
        u = User.objects.get(username=user)
        u.set_password(user_password)
        u.save() 
        return HttpResponse('پسورد شما تغییر یافت  ')



def get_mail(request):
    if request.method=='GET':
        return render(request,"resetpassword/get_mail.html")
    else:
        global user
        user = request.POST.get('username')
        u = User.objects.get(username=user)
        if request.POST.get('mail') == u.email:
            send_mail('code',random_code,settings.EMAIL_HOST_USER,[request.POST.get('mail')]) 

            return HttpResponseRedirect('faramooshi')
        else:
            context={'message':'نام کاربری و ایمیل با هم مطابقت ندارند'}
            
            return render(request,"resetpassword/get_mail.html",context)
        


def signup_user(request):

    form = SignUpform()
    if request.method == "POST":
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password1)
            messages.success(request,('حساب کاربری شما ساخته شد'))
            login(request=request,user=user)
            return redirect("login")
        
        else:
            messages.success(request,('ثبت نام شما با مشکل مواجه شد'))
            return redirect("signup")
    else:

        return render(request,'resetpassword/signup.html',{'form':form})