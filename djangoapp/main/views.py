from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from main.forms import UserCreationForm
from .models import Task
from main.forms import TaskForm

def home(request):
    tasks = Task.objects.order_by('title')
    return render(request, 'home.html', {'title': 'Главная страница сайта', 'tasks': tasks})


class Signup(View):

    template_name = 'registration/signup.html'

    def get(self, request):
        context = {
            'form': UserCreationForm
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
class Create():

    def create(request):
        error = ''
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.author = request.user.username
                form.save()
                return redirect('home')
            else:
                error = 'Форма некорректна'
    
        form = TaskForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'main/create.html', context)