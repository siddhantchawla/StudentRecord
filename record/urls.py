from django.urls import path

from . import views

urlpatterns = [

	path('home/',views.index),
	path('list/',views.list),
	path('scan/',views.scan),

]