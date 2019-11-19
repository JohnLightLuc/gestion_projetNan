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