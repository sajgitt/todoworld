from django.shortcuts import render
from django.shortcuts import redirect,render
from .models import ToDoList


# Create your views here.

def add_list(request):
    if request.method=='POST':
        Title=request.POST.get('Title')
        todo=ToDoList.objects.create(
        Title=Title
        )  
        todo.save()
        return redirect('showtodo')
    return render(request,'showtodolist.html')
 

def showtodo(request):
    dict_disp={
        'disp':ToDoList.objects.all()
    }
    return render(request,'showtodolist.html',dict_disp)


def del_todo(request,k1):
    Title=ToDoList.objects.get(id=k1)
    if request.method=='POST':
        Title.delete()
        return redirect('/')
    context={
        'title':Title
    }
    return render(request,'del_todo.html',context)
    
