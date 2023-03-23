from django.urls import path, include
from main.views import Signup, Create
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', include('django.contrib.auth.urls')),
    path('signup', Signup.as_view(), name='signup'),
    path('create', Create.create, name='create'),
]