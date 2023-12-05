
from .views import *
from django.urls import path

urlpatterns = [
    path('', home , name='home'),
    path('news/<str:slug>',news,name='news'),
    path('search/',search,name='search')
    
]


