from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Categorie(models.Model):

    def __str__(self):
        return self.categorie_name

    categorie_name = models.CharField(max_length=100,null=False, default='rien')



class Aliment(models.Model):

    def __str__(self):
        return self.product_name

    product_name = models.CharField(max_length=200, null=False,default='erreur')
    code = models.CharField(max_length=100, null=False, unique=True, default='erreur')
    nutrition_score = models.CharField(max_length=10, null=False, default='erreur')
    #id_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=100, null=False, default='erreur')
    url_img_small = models.URLField(max_length=200, null=True)
    url_img_big = models.URLField(max_length=200, null=True)
    url_thumb_url = models.URLField(max_length=200, null=True)
    saturated_fat_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )

class Substitution(models.Model):

    def __str__(self):
        return self.id_aliment

    id_aliment = models.ForeignKey(Aliment, on_delete=models.CASCADE, related_name='id_aliment')
    id_aliment_substitution = models.ForeignKey(Aliment, on_delete=models.CASCADE, related_name='id_aliment_substitution')
    # id_aliment = models.PositiveIntegerField(null=False)
    # id_aliment_substitution = models.PositiveIntegerField(null=False)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)