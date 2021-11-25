from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add-user/', views.add_user),
    path('login/', views.login),
    path('logout/', views.logout),
    path('wall/', views.wall, name="wall")
]
