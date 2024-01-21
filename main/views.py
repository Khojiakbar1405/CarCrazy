from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from . import models


# front
def index(request):
    context = {}
    if request.method == 'POST':
        body = request.POST['body']
        name = request.POST['name']
        email = request.POST['email']
        models.Form.objects.create(
            body = body,
            name = name,
            email = email,
        )
        return redirect('teams')
    return render(request, 'front/index.html', context)

def dashboard(request):
    context = {}
    return render(request, 'dashboard/index.html', context)

def create_team(request):
    if request.method == 'POST':
        models.Team.objects.create(
            name=request.POST['name']
        )
        return redirect('teams')
    return render(request, 'dashboard/team/create.html')


def teams(request):
    regions = models.Team.objects.all()
    return render(request, 'dashboard/team/list.html', {'teams':teams})


def team_update(request, id):
    team = models.Team.objects.get(id=id)
    if request.method == 'POST':
        team.name = request.POST['name']
        team.save()
        return redirect('teams')
    return render(request, 'dashboard/team/update.html', {'team':team})


def team_delete(request, id):
    models.Team.objects.get(id=id).delete()
    return redirect('teams')

# items
def work_create(request):

    if request.method == 'POST':
        image = request.FILES['image']
        models.Work.objects.create(
            image=image
        )
        return redirect('works')
    return render(request, 'dashboard/works/create.html',)


def works(request):
    works = models.Work.objects.all()
    context = {
        'works':works
    }
    return render(request, 'dashboard/works/list.html', context)


def work_update(request, id):
    work = models.Work.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES.get('image')
        if image:
            work.image = image
            work.title = title
        work.save()

    context = {
        'work':work,
    }
    return render(request, 'dashboard/works/update.html', context)


def work_delete(request, id):
    models.Work.objects.get(id=id).delete()
    return redirect('works')


def appeal_dashboard(request):
    appeal= models.Form.objects.all()
    context = {
        'appeal':appeal
    }
    return render(request, 'dashboard/appeal/list.html', context)

def appeal_delete(request, id):
    models.Form.objects.get(id=id).delete()
    return redirect('appeal_dashboard')

def register_user(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        return redirect('dashboard')
    return render(request, 'dashboard/auth/register.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('index')