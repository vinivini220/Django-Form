from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm


def home(request):
    task=Task.objects.all()  
    return render(request,'home.html',{'task':task})


def add_task(request):
    form=TaskForm()
    if request.method == 'POST':
       form=TaskForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
    return render(request,'add_task.html',{'form':form})





def edit_task(request,id):
    task=get_object_or_404(Task,id=id)
    form=TaskForm(instance=task) 
    if request.method == 'POST':
       form=TaskForm(request.POST,instance=task)
       if form.is_valid():
           form.save()
           return redirect('home')
    return render(request,'edit.html',{'form':form})


def delete_task(request,id):
    task=get_object_or_404(Task,id=id)
    task.delete()
    return redirect('home')



