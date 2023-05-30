from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from main.forms import UserCreationForm
from .models import Task
from .documents import TaskDocument
from main.forms import TaskForm

def home(request):
    text_search = request.GET.get('search')
    if text_search:
        s_ta = TaskDocument.search().query("match_phrase", task=text_search).to_queryset()
        s_ti = TaskDocument.search().query("match_phrase", title=text_search).to_queryset()
        tasks = (s_ta | s_ti).distinct()
    else:
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
        form = TaskForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.author = request.user
                title_name = form.cleaned_data['title']
                task_name = form.cleaned_data['task']
                form = Task(title=title_name, task=task_name, author=form.author)
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