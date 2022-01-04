from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView


class AnotherPageView(TemplateView):
    template_name = "another.html"


class AboutPageView(TemplateView):
    template_name = 'about.html'


def homePageView(request):
    return render(request, template_name='base.html')


def advenn(request):
    return HttpResponse("<b>Advenn,Adv</b>")


def base(request):
    return render(request, template_name='base.html')
