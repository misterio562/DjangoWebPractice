from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def index(request):
    title = "página hecha con Django!"
    return render(request, 'index.html',{
        'title': title,
    })

def hello(request, username):
    print(username)
    return HttpResponse(f'<h1>Hello world! {username}</h1>')

def about(request):
    return render(request, 'about.html')

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

def tasks(request):
    # tasks = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        form = CreateNewTask
        return render(request, 'tasks/create_task.html', {
            'form': form
        })
    else:
        Task.objects.create(title=request.POST['title'],
        description = request.POST['description'],
        project_id = 1)
        return redirect('tasks')
        
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
            'form': CreateNewProject
        })
    else:
        project = Project.objects.create(name = request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id = id)
    print(tasks)
    return render(request, 'projects/detail.html',{
        'project': project,
        'tasks': tasks
    })    