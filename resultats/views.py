from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from compte.forms import ContactForm
from django.contrib.auth import logout
from compte.models import Aliment as AlimentModel
from django.db import models,IntegrityError
from libs.API import *

# Create your views here.
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def afficher_resultats(request):
    template = loader.get_template('resultats/resultats.html')

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        data = request.POST.get("name")

        query = AlimentModel.objects.filter(product_name__icontains = data)

        print(type(query))
        #if query.exist():
        if query:
            aliment_search = query
            print(query)

        else:
            API_data_aliment = load_data_OFF(data)
            aliment_search = Aliment(API_data_aliment[0])
            #prendre que les groupe en fr: ?

            API_data_categorie = load_data_from_category_OFF(aliment_search.categorie)



            try:
                insert_db = AlimentModel.objects.create(
                    product_name=aliment_search.product_name,
                    code=aliment_search.code,
                    nutrition_score=aliment_search.nutrition_grades,
                    categorie=aliment_search.categorie,
                    url_img_small=aliment_search.image_small_url,
                    url_img_big=aliment_search.image_front_url,
                    url_thumb_url=aliment_search.image_front_thumb_url,
                    saturated_fat_100g=aliment_search.fat

                )
            except IntegrityError:
                pass



            for product in API_data_categorie:
                aliment = Aliment(product)
                try:
                    insert_db = AlimentModel.objects.create(
                        product_name=aliment.product_name,
                        code = aliment.code,
                        nutrition_score =aliment.nutrition_grades,
                        categorie = aliment.categorie,
                        url_img_small = aliment.image_small_url,
                        url_img_big = aliment.image_front_url,
                        url_thumb_url =aliment.image_front_thumb_url,
                        saturated_fat_100g = aliment.fat

                        )
                except IntegrityError:#in case of code duplicate
                    pass


        #if:
            ##query dans la DB avec des %names%
            ## si ca me ramene qqchose, je le garde et vais chercher dans la meme categorie un objet mieux
            #aliment_search = data
        #else: la query en db ne me ramene rien
            ## je vais dasn l API et ramene le premier objet
            # je retourne chercher les 20 objets de la meme categories et sauve tout en base
            # j affiche le premier objet + le plus sains
        #aliment_search = load_data_OFF(data)



        context = {
            'aliment_search': aliment_search
        }

    else:

        #si pas via POST

        form = ContactForm()

        context = {
            'aliment_search': 'CHEPAS'
        }

    return HttpResponse(template.render(context, request=request))






def substitution(request,code_aliment):
    template = loader.get_template('resultats/substitution.html')
    id = int(code_aliment)  # make sure we have an integer.

    aliment_a_substituer = AlimentModel.objects.get(code=id)
    score_aliment_aliment_a_substituer = aliment_a_substituer.nutrition_score
    list_aliment_substitution = AlimentModel.objects.filter(categorie=aliment_a_substituer.categorie)\
    .values_list('code','nutrition_score')

    #list_aliment_substitution.remove(id)#remove aliment que l on veut substituer

    for element in list_aliment_substitution:
        if element[1] < score_aliment_aliment_a_substituer and element[0]!=id:
            element_de_substitution = element
            break
        else:
            element_de_substitution = 'rien trouver comme substituion'





    print (list_aliment_substitution)
    print(id)
    #aliment_substitution = AlimentModel.objects.get(code=id)


    context = {
        'categorie_substituion': element_de_substitution
    }

    return HttpResponse(template.render(context, request=request))
