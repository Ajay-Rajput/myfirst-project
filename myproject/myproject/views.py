from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from todo_list.models import todo



def Todo(request):
    try: 
    
        title=request.POST['title']
        description=request.POST['description']
       

        e=todo(title=title, description=description)
        e.save()
    
    except Exception as e:
        print(e)

        
    return render(request, 'todo.html')


def tt(response):
    do=todo.objects.all()

    data={
         'do':do
     }
    return render(response, 'tt.html',data)



def addtodo(request):
    try:    
        title=request.POST['title']
        description=request.POST['description']

        e=todo(title=title, description=description)
        e.save()
        return redirect("/tt")
    except Exception as e:
        print(e)

def updatetodo(request,id):
    try:    
        title=request.POST['title']
        description=request.POST['description']

        e=todo(id=id, title=title, description=description)
        e.save()
        return redirect("/tt")
    except Exception as e:
        print(e)
def deletetodo(request,id):
    todo.objects.filter(id=id).delete()
    
    return redirect("/tt")

def complet_do(request, id):
    print(id)
    Todo=todo.objects.get(id=id)
    Todo.completed=True
    Todo.save()

    return redirect("/tt")

  













