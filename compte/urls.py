from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from compte import views



urlpatterns = [

    url(r'^$', views.index), # "/store" will call the method "index" in "views.py"
    url(r'^creation$', views.creation), # "/store" will call the method "index" in "views.py"

]