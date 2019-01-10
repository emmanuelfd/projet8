from django.db import models

# Create your models here.

class Account(models.Model):

    def __str__(self):
        return self.user_name

    user_name = models.EmailField(max_length=100,null=False)
    password = models.CharField(max_length=50,null=False)
    created_at = models.DateTimeField(auto_now_add=False)


class Categorie(models.Model):

    def __str__(self):
        return self.categorie_name

    categorie_name = models.CharField(max_length=100,null=False)



class Aliment(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, null=False)
    nutrition_score = models.CharField(max_length=10, null=False)
    id_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    url_img_small = models.URLField(max_length=200, null=True)
    url_img_big = models.URLField(max_length=200, null=True)
    carbohydrates_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    carbohydrates_unit = models.CharField(max_length=10, null=True)
    carbohydrates_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    carbohydrates_unit = models.CharField(max_length=10, null=True)
    proteins_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    proteins_unit = models.CharField(max_length=10, null=True)
    energy_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    energy_unit = models.CharField(max_length=10, null=True)
    sodium_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    sodium_unit = models.CharField(max_length=10, null=True)
    fiber_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    fiber_unit = models.CharField(max_length=10, null=True)
    sugars_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    sugars_unit = models.CharField(max_length=10, null=True)
    saturatedfat_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    saturatedfat_unit = models.CharField(max_length=10, null=True)
    fat_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    fat_unit = models.CharField(max_length=10, null=True)
    salt_100g = models.DecimalField(null=True, max_digits=10,decimal_places=3 )
    salt_unit = models.CharField(max_length=10, null=True)

class Substitution(models.Model):

    def __str__(self):
        return self.id_aliment

    id_aliment = models.ForeignKey(Aliment, on_delete=models.CASCADE, related_name='id_aliment')
    id_aliment_substitution = models.ForeignKey(Aliment, on_delete=models.CASCADE, related_name='id_aliment_substitution')
    # id_aliment = models.PositiveIntegerField(null=False)
    # id_aliment_substitution = models.PositiveIntegerField(null=False)
    user_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)