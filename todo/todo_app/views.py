from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from todo_app.models import Todo
from todo_app.forms import TODOForm
import datetime
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = Todo.objects.filter(user=user).order_by('priority')
        return render(request , 'index.html' , context = {'form' : form , 'todos':todos}) 

def login(request):
    if request.method =="GET":
        form1 = AuthenticationForm()
        context = {
            'form' : form1
            }
        return render(request , 'login.html',context=context)
    
        
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)

            if user is not None:
                loginUser(request , user)
                return redirect('home')

        else:
            #form = UserCreationForm(request.POST)
            context = {
                        'form' : form
                     }
            return render(request , 'login.html' , context = context)



def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form' : form
        }
    
        return render(request , 'signup.html' , context = context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            'form' : form
        }
    
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('home')
        else:
            return render(request , 'signup.html' , context=context)
        
@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
    form = TODOForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        todo = form.save(commit=False)
        todo.user = user
        todo.save()
        print(todo)
        return redirect("home")
    else:
         
        return render(request , 'index.html' , context = {'form' : form})

def signout(request):
    logout(request)
    return redirect('login')


def delete_todo(request , id):
    Todo.objects.get(pk = id).delete()
    return redirect('home')


def change_todo(request , id, status):
    todo =  Todo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')



