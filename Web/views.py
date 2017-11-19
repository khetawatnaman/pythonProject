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
        cat=request.POST['category']
        gen=request.POST['genre']
        vu="static/videos/"+request.POST['video_url']
        iu = "static/images/"+request.POST['image_url']
        p = Video(title=t,description=d,duration=dur,category=cat,video_url=vu,image_url=iu,genre=gen)
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

image=[]

def home(request):
    a = list(Video.objects.order_by("-viewCount").values_list())[:8]
    trending=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        trending.append(local)
    a = list(Video.objects.order_by("-created_at").values_list())[:8]
    new = []
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        new.append(local)
    n = range(len(a))
    return render(request, 'home.html', {'n':n,'trending': trending,'new':new})

def videoviewing(request):
    if request.method == "POST":
        video=request.POST['abc']
        a=Video.objects.filter(title=video).values_list()[0]
        video=a[8]
        t=a[0]
        dur=a[11]
        des=a[7]
        cat=a[5]
        gen=a[12]
        views=a[4]
        like = a[2]
        dislike = a[3]
        a=Video.objects.filter(category=cat).values_list()
        a=a.order_by("-viewCount")[:5]
        related=[]
        for i in range(len(a)):
            local=[]
            if a[i][9]!=t:
                local.append(a[i][9])
                local.append(a[i][0])
                local.append(a[i][4])
                related.append(local)
        if len(a)<5:
            b=5-len(a)
            a = Video.objects.filter(category=cat).values_list()
            a = a.order_by("-viewCount")[:b]
            for i in range(len(a)):
                local=[]
                if a[i][9]!=t:
                    local.append(a[i][9])
                    local.append(a[i][0])
                    local.append(a[i][4])
                    if local not in related:
                        related.append(local)
    n= range(5)
    return render(request, 'Video Viewing.html', {'related':related,'n':n,'video':video,'t':t,'dur':dur,'des':des,'views':views,'like':like,'dislike':dislike})

def about(request):
    return render(request, 'About.html', context=None)

def bollywood(request):
    a=list(Video.objects.filter(category="Bollywood").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def hollywood(request):
    a=list(Video.objects.filter(category="Hollywood").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def punjabi(request):
    a=list(Video.objects.filter(category="Punjabi").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def rock(request):
    a=list(Video.objects.filter(genre="Rock").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def blues(request):
    a=list(Video.objects.filter(genre="Blues").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def pop(request):
    a=list(Video.objects.filter(genre="Pop").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def edm(request):
    a=list(Video.objects.filter(genre="EDM").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def classical(request):
    a=list(Video.objects.filter(genre="Classical").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def hiphop(request):
    a=list(Video.objects.filter(genre="Hip Hop").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def rap(request):
    a=list(Video.objects.filter(genre="Rap").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})

def rnb(request):
    a=list(Video.objects.filter(genre="Rhythm n Blues").values_list())[:5]
    image=[]
    for i in range(len(a)):
        local=[]
        local.append(a[i][9])
        local.append(a[i][0])
        local.append(a[i][4])
        image.append(local)
    return render(request, 'Search Results.html', {'image':image,'search':search})