from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt
from django.apps import apps

# Create your views here.
def index(request):
    return render(request, "index.html")

def wall(request):
    if 'id' in request.session:
        post_wall = apps.get_model('wall.Message').objects.all()
        if post_wall:
            context = {
                'wall_messages': reversed(post_wall),
                'user': User.objects.get(id=request.session['id'])
            }
        else:
            context = {
                'user': User.objects.get(id=request.session['id'])
            }
        return render(request, 'wall/index.html', context)
    else:
        return redirect('index')

def add_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('index')
    else:
        User.objects.create(
            first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(
                request.POST["password"].encode(), bcrypt.gensalt()
            ).decode()
        )
        request.session['id'] = User.objects.last().id
        return redirect('wall')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login")
        return redirect('index')
    else:
        user = User.objects.filter(email=request.POST['email_login'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['pw_login'].encode(), logged_user.password.encode()):
                request.session['id'] = logged_user.id
                return redirect('wall')
            else:
                messages.error(request, "Incorrect password.", extra_tags="login")
                return redirect('index')
        else:
            messages.error(request, "Incorrect email.", extra_tags="login")
            return redirect('index')

def logout(request):
    request.session.flush()
    return redirect('index')