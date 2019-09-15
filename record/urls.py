from django.urls import path

from . import views

urlpatterns = [

	path('home/',views.index),
	path('scan/',views.scan),
	path('list/',views.list),


]