from rango.forms import CategoryForm, UserForm, UserProfileForm
from django.shortcuts import render
from rango.models import category,page
from django.http import HttpResponse

def index(request):
	
	category_list = category.objects.order_by('-likes')[:5]
	pages_list = page.objects.order_by('-views')[:5]
	context_dict = {'categories': category_list}
	context_dict['pages'] = pages_list
	# Render the response and send it back!
	
	return render(request,'rango/index.html',context = context_dict)

def homeofrango(request):
	return HttpResponse("THis is my home of rango page.")

def about(request):
	
	dict_about = {'Intro':"This is Rango app and I am the about section of the app"}
	return render(request,'rango/about.html', context=dict_about)

def show_category(request, category_name_slug):
	context_dict = {}
	try:

		cat = category.objects.get(slug = category_name_slug)#throws exception if category not found.
		pag = page.objects.filter(category = cat)#returns empty list not found any pages. 

		context_dict['category']=cat
		context_dict['pages'] = pag

	except:

		context_dict['category']=None
		context_dict['pages'] = None

	return render(request, 'rango/category.html', context = context_dict)

def add_category(request):
	form = CategoryForm()

	if request.method =='POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)

		else:
			print(form.errors)

	return render(request, 'rango/add_category.html', {'form': form})		

def register(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
	
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()


			profile = profile_form.save(commit=False)

			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
		
			registered = True
		else:
			print(user_form.errors, profile_form.errors)	
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,'rango/register.html',{'user_form': user_form,'profile_form': profile_form,'registered': registered})	
