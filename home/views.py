from django.shortcuts import render
from home.models import Blogpost , Contect
from django.contrib import messages


# Create your views here.

def home(request):
    posts = Blogpost.objects.filter(publish=True)
    context = {'posts': posts}
    return render(request, "home.html", context)


def blog(request):
    posts = Blogpost.objects.filter(publish=True)
    context = {'posts': posts}
    return render(request, "blog.html", context)


def blogview(request, slug):
    posts = Blogpost.objects.filter(slug=slug).first()
    context = {'posts': posts}
    return render(request, "pview/blogview.html", context)


def contect(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        Lname = request.POST['lname']
        mob = request.POST['mobile']
        email = request.POST['email']
        desc = request.POST['description']
        if len(fname) < 3 or len(Lname) < 3 or len(mob) < 10 or len(email) < 5 or len(desc) < 5:
            messages.error(request, 'Please fill the form correctly')
        else:
            contect = Contect(fname=fname, Lname=Lname , mob=mob,
                              email=email, desc=desc,)
            contect.save()
            messages.success(request, 'Your messages has Submited Successfuly')
    return render(request, "contect.html")


def about(request):
    return render(request, "about.html")
