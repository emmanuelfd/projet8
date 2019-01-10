from django.shortcuts import render
from .models import Account

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('compte/accueil_compte.html')
    compte = Account.objects.filter(user_name = "manu@hotmail.com")

    #return HttpResponse(template.render(request=request))
    return HttpResponse(compte)

    if request.method == 'POST':

        email = request.POST.get('email')
        name = request.POST.get('login')