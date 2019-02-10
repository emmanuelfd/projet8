from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from . import views##


app_name = 'compte'

urlpatterns = [

    url(r'^$', views.index, name='acceuil'),
    url(r'^creation$', views.creation, name='creation'),
    url(r'^logout$', views.deconnexion, name='logout'),

]