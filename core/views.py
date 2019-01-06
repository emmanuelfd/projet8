from django.http import HttpResponse
from django.template import loader


def home1(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)

def home(request):
    template = loader.get_template('core/accueil.html')
    return HttpResponse(template.render(request=request))