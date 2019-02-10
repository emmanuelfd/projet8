from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from compte.forms import ContactForm
from django.contrib.auth import logout
import os

# Create your views here.
from django.http import HttpResponse
from django.template import loader

#LOGIN_REDIRECT_URL = '/' => redirect after login

def index(request):
    template = loader.get_template('compte/accueil_compte.html')

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm(request.POST)
        error = False

        if form.is_valid():

            username = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(username=username,
                                password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons

            else:  # sinon une erreur sera affichée
                error = True

            context = {
                'error': error,
                'user' : user
            }

    else:

        form = ContactForm()

        context = {
            'form': form
        }


    return HttpResponse(template.render(context,request=request))





def creation(request):
    template = loader.get_template('compte/creation_compte.html')

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm(request.POST)

        if form.is_valid():

            compte = request.POST.get('name')
            pwd = request.POST.get('password')
            user = User.objects.create_user(compte,'',pwd)
            user.save()

            context = {
                'envoi': True
            }

        #else:
         #   context['errors'] = form.errors.items()

    else:

        form = ContactForm()

        context = {
            'form': form
        }


    return HttpResponse(template.render(context,request=request))


def deconnexion(request):
    template = loader.get_template('compte/logout.html')
    logout(request)
    return HttpResponse(template.render( request=request))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


test = [os.path.join(BASE_DIR, 'core/static/')]

print(test)