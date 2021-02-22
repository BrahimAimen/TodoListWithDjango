from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.


def todoview(request):
    todo_items_obj = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': todo_items_obj})


def addtodo(request):
    c = request.POST['content']
    new_item = TodoItem(content=c)
    new_item.save()
    return(HttpResponseRedirect('/todo/'))


def deletetodo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    item.delete()
    return(HttpResponseRedirect('/todo/'))
