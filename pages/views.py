from django.shortcuts import render

from django.http import HttpResponse

from .models import Project, Actu, About

from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    
    projects = Project.objects.all().order_by('classement')
    
    
    context = {
        
        'projects': projects,

    }
    
    return render(request, 'pages/index.html',context)


def about(request):
    
    
    abouts = About.objects.all()
    
    context = {
        'abouts': abouts,
    }
    
    return render(request, 'pages/about.html', context)


def contact(request):
    return render(request, 'pages/contact.html')


def cont(request):
    return render(request, 'pages/cont.html')

def actu(request):
    
    actus = Actu.objects.all()
    
    context = {
        
        'actus': actus,

        }
    
    return render(request, 'pages/actu.html', context)



def detail(request, project_id):
    
    project = get_object_or_404(Project, pk=project_id)
    
    context = {
        'project': project,
    }
    
    return render(request, 'pages/project.html', context)