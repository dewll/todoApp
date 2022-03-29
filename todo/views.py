from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def home(request):
    '''
    This is a home view function that render the todo list object
    depending on what is input on the search box and if None it return
    all the columns in the database
    '''
    if 'q' in request.GET: #check if the request.GET is to search for todo
        q = request.GET['q']
        todo = models.Todo.objects.filter(title__icontains=q) #query the db by q
    else:
        todo  = models.Todo.objects.all() #query all to inside the database
    return render(request, 'todo/home.html', {'todo_lists':todo}) #render home.html and render the todo_list context
    if request.POST: #check if it is HTTP POST request
        if 'add_todo' in request.POST: #check if the request is to add todo
            title = request.POST['title'] #get the title from the POST request
            description = request.POST['description'] #get the description from the POST request
            completed = request.POST['completed'] #get the status of todo from the POST request if FALSE OR TRUE
            models.Todo.objects.create(title=title,description=description,completed=completed) # save into database
            return redirect('/') #return to the home page 
def detail(request, pk):
    '''
    This is a detail view function that render the todo list object
    depending on the primary key of object in the database, and from
    this detail view you can update or delete the object
    '''
    details = models.Todo.objects.get(pk=pk)
    if request.POST: #check if it is HTTP POST request
        if 'update' in request.POST: #check if the request is to update todo
            title = request.POST['title'] #get the title from the POST request
            description = request.POST['description'] #get the description from the POST request
            completed = request.POST['completed'] #get the status of todo from the POST request if FALSE OR TRUE
            models.Todo.objects.filter(pk=pk).update(title=title,description=description,completed=completed) #update and save into database
            return redirect('/') #return to the home page 
    if request.POST:
        if 'delete' in request.POST: #check if it is HTTP POST request
            try:
                models.Todo.objects.get(pk=pk).delete()
                return redirect('/')
            except:
                pass
    return render(request, 'todo/detail.html', {'details':details})
    
        


