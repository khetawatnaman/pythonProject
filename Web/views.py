from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Video,User

def login(request):
    return render(request, 'index.html', context=None)

def naman(request):
    return render(request, 'Naman.html', context=None)

def hitesh(request):
    return render(request, 'Hitesh.html', context=None)

def nishit(request):
    return render(request, 'Nishit.html', context=None)

def abhya(request):
    return render(request, 'Abhya.html', context=None)

def agrima(request):
    return render(request, 'Agrima.html', context=None)

def piyush(request):
    return render(request, 'Piyush.html', context=None)

def praman(request):
    return render(request, 'Naman.html', context=None)

def prashant(request):
    return render(request, 'Prashant.html', context=None)

def shivani(request):
    return render(request, 'Shivani.html', context=None)

def channel(request):
    if request.method == "POST":
        t=request.POST['songname']
        d=request.POST['description']
        dur=request.POST['duration']
        cat=request.POST['gender']
        vu=request.POST['video_url']
        iu = request.POST['image_url']
        p = Video(title=t,description=d,duration=dur,category=cat,video_url=vu,image_url=iu)
        p.save()
    return render(request, 'channel.html', context=None)

def upload(request):
    return render(request, 'upload.html', context=None)

def search(request):
    if request.method == "POST":
        search = request.POST['query']
        a = list(Video.objects.all().values_list())
        image=[]
        for i in range(len(a)):
            if search in a[i][7]:
                local = []
                local.append(a[i][9])
                local.append(a[i][0])
                local.append(a[i][4])
                image.append(local)
        n = range(4)
        return render(request, 'Search Results.html', {'n':n,'image':image,'search':search})

def home(request):
    a = list(Video.objects.all().values_list())
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    n = range(len(a))
    return render(request, 'home.html', {'n':n,'image': image})


def videoviewing(request):
    a="static/videos/movie.mp4"
    if request.method == "POST":
        t =  ""
    n = range(5)
    return render(request, 'Video Viewing.html', {'a':a,'n':n})

def about(request):
    return render(request, 'About.html', context=None)