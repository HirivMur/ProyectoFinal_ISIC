from django.conf.urls import url
from views import loginproy
from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    url(r'^$', login, {'template_name':'login.html'}, name="loginproy"),

]
