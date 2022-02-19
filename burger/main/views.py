from django.shortcuts import render
from .models import New, Galery
from django.utils import timezone

def glavnaya(request):
	return render(request, 'main/glavnaya.html',{})


def Galery_page(request):
	data = Galery.objects.all()
	return render(request, 'main/galery.html',{'data':data})


def News(request):
	posts = New.objects.all()
	return render(request, 'main/news.html',{'posts': posts})


def About(request):
	return render(request, 'main/about.html',{})