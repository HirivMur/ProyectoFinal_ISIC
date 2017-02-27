from django.conf.urls import url
from docentes.views import listaDocentes


urlpatterns = [
    url(r'^$', listaDocentes, name="listaDocentes"),

]
