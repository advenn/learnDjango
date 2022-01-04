from django.http import HttpResponse
from django.urls import path
import hello.views

urlpatterns = [
    path('adv/', hello.views.advenn, name='test'),
    path('', hello.views.homePageView,name='home'),
]