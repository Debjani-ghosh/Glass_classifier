
from django.contrib import admin
from django.urls import path
from . import views # . is root 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home") ,# this means when path is empty ,home is shown..name is optional.
    path('result/',views.result,name="result")
]
