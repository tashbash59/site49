from django.urls import path
from . import views

urlpatterns = [
	path('', views.glavnaya, name='glavnaya'),
	path('news/', views.News, name='news/'),
	path('galery/', views.Galery, name='galery/')
]