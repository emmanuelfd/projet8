from django.shortcuts import render
from .models import Account
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('compte/accueil_compte.html')
    compte = Account.objects.filter(user_name = "manu@hotmail.com")

    #return HttpResponse(template.render(request=request))
    return HttpResponse(template.render(request=request))



    if request.method == 'POST':

        pwd = request.POST.get('password')
        name = request.POST.get('login')


    elif request.method == 'POST':

        pwd = request.POST.get('password')
        name = request.POST.get('login')

        user = User.objects.create_user(name,pwd,email=None)


def creation(request):
    template = loader.get_template('compte/creation_compte.html')

    return HttpResponse(template.render(request=request))

