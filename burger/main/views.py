from django.shortcuts import render
from .models import New
from django.utils import timezone

def glavnaya(request):
	return render(request, 'main/glavnaya.html',{})


def Galery(request):
	return render(request, 'main/galery.html',{})


def News(request):
	posts = New.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'main/news.html',{'posts': posts})