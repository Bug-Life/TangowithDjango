from django.shortcuts import render
from models import category,page
from django.http import HttpResponse

def index(request):
	
	category_list = category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	# Render the response and send it back!
	
	return render(request, 'rango/index.html',context = context_dict)

def homeofrango(request):
	return HttpResponse("THis is my home of rango page.")

def about(request):
	
	dict_about = {'Intro':"This is Rango app and I am the about section of the app"}
	return render(request,'rango/about.html', context=dict_about)