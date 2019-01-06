from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('compte/accueil_compte.html')
    return HttpResponse(template.render(request=request))


def initial(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        name = request.POST.get('login')