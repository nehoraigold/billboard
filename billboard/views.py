from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import get_recent_posts, Billboard
from .forms import BillboardForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def home(request):
    return render(request, "billboard/home.html", {"posts": get_recent_posts(), "form": BillboardForm()})


def new_post(request):
    post = BillboardForm(request.POST)
    print(post)
    if post.is_valid():
        print(post.is_valid())
        new_billboard = post.save()
    return HttpResponseRedirect('/billboard/')

def register(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            # login(request, user)
            return HttpResponseRedirect('/billboard/')
    else:
        return render(request, 'registration/register.html', {"form": UserCreationForm()})