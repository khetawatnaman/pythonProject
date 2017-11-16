from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.login, name= 'login'),
    url(r'naman', views.naman, name='naman'),
    url(r'hitesh', views.hitesh, name='hitesh'),
    url(r'nishit', views.nishit, name='nishit'),
    url(r'abhya', views.abhya, name='abhya'),
    url(r'agrima', views.agrima, name='agrima'),
    url(r'praman', views.praman, name='praman'),
    url(r'piyush', views.piyush, name='piyush'),
    url(r'prashant', views.prashant, name='prashant'),
    url(r'shivani', views.shivani, name='shivani'),
    url(r'channel', views.channel, name='channel'),
    url(r'home', views.home, name='home'),
    url(r'videoviewing', views.videoviewing, name='videoviewing'),
    url(r'about', views.about, name='about'),
    url(r'search', views.search, name='search'),
    url(r'upload', views.upload, name='upload'),
]
