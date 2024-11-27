from multiprocessing import context
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render

from resumes.forms import AddResumeForm

# Create your views here.

def index(request: WSGIRequest ):
    return HttpResponse('JJJJ')

def detail(request: WSGIRequest, pk):
    return HttpResponse('JJJ2')

def add(request: WSGIRequest):
    if request.method == "GET":
        form = AddResumeForm()
        context={"form":form}
        return render(request, 'add.html', context)
    
    if request.method == "POST":
        form.AddResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        context={"form":form}
        return render(request, 'add.html', context)
    

    return HttpResponse('Method not allowed')
