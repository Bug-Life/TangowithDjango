from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner!" + '<a href="/rango/about">About.</a>')

def homeofrango(request):
	return HttpResponse("THis is my home of rango page.")

def about(request):
	return HttpResponse("Rango says here is the about page." + '<a href="/rango/">Main Page.</a>');