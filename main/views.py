from django.shortcuts import render

def index(request):
    context = {}
    return  render(request, 'index.html', context)

def projects(request):
    context = {}
    return  render(request, 'projects.html', context)

def languages(request):
    context = {}
    return render(request, 'languages.html',context)

def skills(request):
    context = {}
    return render(request, 'skills.html',context)

def logicstrength(request):
    context = {}
    return render(request, 'logicstrength.html',context)

def logiccourses(request):
    context = {}
    return render(request, 'logiccourses.html',context)    
def programmingstrength(request):
    context = {}
    return render(request,'programmingstrength.html',context)
def programmingcourses(request):
    context = {}
    return render(request,'programmingcourses.html',context)
def technicalstrength(request):
    context = {}
    return render(request,'technicalstrength.html',context)
def technicalcourses(request):
    context = {}
    return render(request,'technicalcourses.html',context)
def communicationstrength(request):
    context = {}
    return render(request,'communicationstrength.html',context)        
def communicationcourses(request):
    context = {}
    return render(request,'communicationcourses.html',context)        
    