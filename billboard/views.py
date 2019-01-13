from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import get_recent_posts
from .forms import BillboardForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def home(request):
    return render(request, "billboard/home.html", {"posts": get_recent_posts(), "form": BillboardForm()})


def new_post(request):
    post = BillboardForm(request.POST)
    print("--------------------------POST REQUEST ------------------------")
    print(post)
    if post.is_valid():
        new_billboard = post.save()
        print("---------------------------NEW BILLBOARD ----------------------------")
        print(new_billboard)
    return HttpResponseRedirect('/billboard/')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect('/billboard/')
        else:
            return render(
                request,
                'registration/register.html',
                {
                    "form": UserCreationForm(),
                    "msg": "The form you submitted could not be processed. Please try again."
                })
    else:
        return render(request, 'registration/register.html', {"form": UserCreationForm()})


def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save()
    return HttpResponseRedirect('/billboard/')