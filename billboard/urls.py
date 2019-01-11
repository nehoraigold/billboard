from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^$', views.home, name="homepage"),
    url(r'^new_post', views.new_post, name='new post'),
    url(r'^login', login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^logout', logout, name='logout')
]