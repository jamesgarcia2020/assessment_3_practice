from django.shortcuts import render
from .models import Todo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"

class TodoDelete(DeleteView):
    model = Todo
    success_url = '/'

class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"