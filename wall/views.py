from django.shortcuts import render, redirect
from .models import Message, Comment
from django.apps import apps

# Create your views here.
# def index(request):
#     return render(request, 'wall/index.html')

def post_message(request):
    logged_user = apps.get_model('login_app.User').objects.filter(id__in=request.POST['user_id'])
    if logged_user:
        Message.objects.create(message=request.POST['message_post'], user=logged_user[0])
    return redirect('wall')

def comment(request):
    user = apps.get_model('login_app.User').objects.filter(id__in=request.POST['user_comment_id'])
    if user:
        Comment.objects.create(
            comment=request.POST['comment'], message=Message.objects.filter(id=request.POST['message_id'])[0], user=user[0]
        )
    return redirect('wall')

def logout(request):
    request.session.flush()
    return redirect('index')