from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from resultats import views


app_name = 'resultats'


urlpatterns = [

    url(r'^$', views.afficher_resultats, name='resultats'),
    url(r'^(?P<code_aliment>[0-9]+)/$', views.substitution, name='substitution'),

]