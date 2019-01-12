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
        new_billboard = post.save()
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