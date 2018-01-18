from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!",'hell':"I am living here"}

	return render(request, 'rango/index.html', context=context_dict)

def homeofrango(request):
	return HttpResponse("THis is my home of rango page.")

def about(request):
	
	dict_about = {'Intro':"This is Rango app and I am the about section of the app"}
	return render(request,'rango/about.html', context=dict_about)
