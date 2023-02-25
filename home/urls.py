from django.contrib import admin
from django.urls import path,include
# from django.urls import views
from home import views
urlpatterns = [
    path('',views.index,name='homme'),
    path('indexx',views.indexx,name='singin'),
    path('home',views.home,name='home'),
    # path('logout',views.logoutuser,name='logoutuser')
]