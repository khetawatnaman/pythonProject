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
    url(r'bollywood', views.bollywood, name='bollywood'),
    url(r'hollywood', views.hollywood, name='hollywood'),
    url(r'punjabi', views.punjabi, name='punjabi'),
    url(r'rock', views.rock, name='rock'),
    url(r'blues', views.blues, name='blues'),
    url(r'pop', views.pop, name='pop'),
    url(r'edm', views.edm, name='edm'),
    url(r'classical', views.classical, name='classical'),
    url(r'hiphop', views.hiphop, name='hiphop'),
    url(r'rap', views.rap, name='rap'),
    url(r'rnb', views.rnb, name='rnb'),
]
