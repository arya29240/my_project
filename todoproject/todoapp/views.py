from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from todoapp.forms import Taskform
from todoapp.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = "object"

class Detailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Updateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse('cbvdetail',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def home(request):
    obj=Task.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        priority = request.POST['priority']
        date=request.POST['date']
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'object':obj})

def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=Taskform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})