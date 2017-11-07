from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.login, name= 'login'),
    url(r'naman', views.naman, name='naman'),
    url(r'hitesh', views.hitesh, name='hitesh'),
    url(r'nishit', views.nishit, name='nishit'),
    # url(r'naman', views.naman, name='naman'),
    # url(r'naman', views.naman, name='naman'),


]
