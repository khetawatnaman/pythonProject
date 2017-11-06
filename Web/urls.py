from django.conf.urls import url, include

from Web import views

urlpatterns = [
    url(r'^$', views.login, name= 'login'),
]
