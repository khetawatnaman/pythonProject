from django import forms
from .models import Video,User

class Send(forms.Form):
    url = forms.CharField(id="query", max_length=100)