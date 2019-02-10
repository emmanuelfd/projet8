from django.http import HttpResponse
from django.template import loader



def home(request):
    template = loader.get_template('core/accueil2.html')
    return HttpResponse(template.render(request=request))

def contact(request):
    template = loader.get_template('core/contact.html')
    return HttpResponse(template.render(request=request))


def mentions_legales(request):
    template = loader.get_template('core/mentions_legales.html')
    return HttpResponse(template.render(request=request))

