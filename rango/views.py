from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

	return render(request, 'rango/index.html', context=context_dict)

def homeofrango(request):
	return HttpResponse("THis is my home of rango page.")

def about(request):
	return HttpResponse("Rango says here is the about page." + '<a href="/rango/">Main Page.</a>');