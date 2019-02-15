# coding: utf-8

import requests
import json
import pdb

#https://fr.openfoodfacts.org/
#https://en.wiki.openfoodfacts.org/API/Read/Product
#https://en.wiki.openfoodfacts.org/API/Read/Search


class Aliment():


    def __init__(self, produit_charge):
        """ to sanitize aliment. will remove apostrophe, set default value (unknown) when missing
        in the openFactfood site. aliment has 5 attributes that will be saved in db
        """

        if produit_charge["categories_hierarchy"] == '':
            self.categorie = 'categorie manquante'
        else:
            #if produit_charge["categories_hierarchy"][-1][2:3] == ':':
             #   self.categorie = produit_charge["categories_hierarchy"][-1][3:].replace("'", "''")

            #else:
               # self.categorie = produit_charge["categories_hierarchy"][-1].replace("'", "''")
            self.categorie = produit_charge["categories_hierarchy"][-1].replace("'", "''")

        try:
            if produit_charge["product_name"] == '':
                self.product_name = 'product name missing'
            else:
                self.product_name = produit_charge["product_name"].replace("'", '-')
        except KeyError:
            self.product_name = 'product name missing'

        if produit_charge["nutriments"] == '':
            self.fat = -1
        else:
            try:
                fat = produit_charge["nutriments"]["saturated-fat_100g"]
                self.fat = int(fat)
            except KeyError:
                self.fat = -1
        if produit_charge["code"] == '':
            self.code = 1
        else:
            self.code = produit_charge["code"]

        if "nutrition_grades" in produit_charge:
            self.nutrition_grades = produit_charge["nutrition_grades"]
        else:
            self.nutrition_grades = ''

        if "image_small_url" in produit_charge:
            self.image_small_url = produit_charge["image_small_url"]
        else:
            self.image_small_url = "Unknown"

        if "image_front_thumb_url" in produit_charge:
            self.image_front_thumb_url = produit_charge["image_front_thumb_url"]
        else:
            self.image_front_thumb_url = "Unknown"

        if "image_front_url" in produit_charge:
            self.image_front_url = produit_charge["image_front_url"]
        else:
            self.image_front_url = "Unknown"


#fichier de configuration pour les url
def load_data_OFF(search_word):
    url = "https://fr.openfoodfacts.org/cgi/search.pl"
    payload = {'search_terms': search_word,'search_simple': '1', 'action': 'process', 'json': '1'}
    #payload = {#'search_terms': search_word,
    #           'tagtype_0': 'categories',
     #          'tag_contains_0': 'contains',
      #         'tag_0': 'pates-a-tartiner',
       #        'search_simple': '1', 'action': 'process', 'json': '1'}

    request = requests.get(url,params=payload)
    dd= request.url

    return_json_API = request.json()#get json file

    product_JSON = return_json_API["products"]  # product_JSON is a list of dico for all aliment

    return product_JSON#return dico with item=code en value list of a,b,c,d


def load_data_from_category_OFF(search_categorie):
    request = requests.get('https://fr.openfoodfacts.org/categorie/' + search_categorie + '/1.json')
    return_json_API = request.json()  # get json file
    product_JSON = return_json_API["products"]  # product_JSON is a list of dico for all aliment


    return product_JSON





#test = load_data_from_category_OFF('pates-a-tartiner')

#test = load_data_OFF('banania')

#print(test)
#print(type(test))

#print(test)


#for product in test:
 #   aliment = Aliment(product)
  #  print(aliment.code)
