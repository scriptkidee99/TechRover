from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    # path('a/',views.indexNew),
    path('blog/',views.blog),
    path('edit/',views.edit),
    path('editor/',views.editor),
    path('users/',views.users),
    path('new/',views.new),
    path('all/',views.all),
    path('favorite/',views.favorite),
    path('verify/',views.verify),
    path('profile/',views.profile)
    
]