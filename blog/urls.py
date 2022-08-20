from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index blog'),
    path('contact/',views.contact,name='contact blog'),
    path('blogpost/<int:id>',views.blogpost,name='blogPost'),
    path('about/',views.about,name='about blog'),
]