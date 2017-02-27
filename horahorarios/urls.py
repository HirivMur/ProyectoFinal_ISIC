from django.conf.urls import url
from horarios.views import listaDocentes


urlpatterns = [
    url(r'^$', listaDocentes, name="listaDocentes"),

]
