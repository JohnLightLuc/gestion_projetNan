from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'page/dashboard/dashboard.html')

def projet(request):
    return render(request, 'page/dashboard/list_projet.html')

def list_user(request):
    return render(request, 'page/dashboard/users.html')

def detailuser(request):
    return render(request, 'page/dashboard/detail_user.html')

def myallprojets(request):
    return render(request, 'page/dashboard/myprojects.html')

def myfinishprojets(request):
    return render(request, 'page/dashboard/mesprojetstermines.html')

def myencoursprojets(request):
    return render(request, 'page/dashboard/mesprojencours.html')

def detailprojet(request):
    return render(request, 'page/dashboard/projetDetail.html')

def connexion(request):
    return render(request, 'page/dashboard/connexion.html')