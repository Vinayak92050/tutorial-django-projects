from django.shortcuts import render,redirect
from .models import Todo,Heading

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    print(todos)
    new_username = Heading.objects.all()
    print(new_username)
    nu_len = len(new_username)
    print (nu_len)
    lastusername = "satoru gojo"
    if nu_len != 0:
        lastusername = new_username[nu_len - 1]
        print(lastusername)  

    
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')    

    return render(request,'index.html',{'todos':todos,'html_username':lastusername})

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def changename(request):
    print(request)
    # username = Heading.objects.get(id=pk)
    # username.save()
    if request.method == 'POST':
        new_username = Heading(
            username = request.POST['username']
        )
        new_username.save()
        return redirect('/')    
    