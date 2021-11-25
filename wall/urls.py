from django.urls import path     
from . import views
urlpatterns = [
    path('wall/', views.index, name='wall'),
    path('post-message/', views.post_message),
    path('wall/comment/', views.comment),
    path('wall/logout/', views.logout)
]