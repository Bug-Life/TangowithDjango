import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'tango_with_django_project.settings')

import django
django.setup()
from rango.models import category, page

def populate():
	# First, we will create lists of dictionaries containing the pages
	# we want to add into each category.
	# Then we will create a dictionary of dictionaries for our categories.
	# This might seem a little bit confusing, but it allows us to iterate
	# through each data structure, and add the data to our models.
	python_pages = [
	{"title": "Official Python Tutorial",
	"url":"http://docs.python.org/2/tutorial/","views":100},
	{"title":"How to Think like a Computer Scientist",
	"url":"http://www.greenteapress.com/thinkpython/", "views":200},
	{"title":"Learn Python in 10 Minutes",
	"url":"http://www.korokithakis.net/tutorials/python/", "views":300} ]

	django_pages = [
	{"title":"Official Django Tutorial",
	"url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views":10},
	{"title":"Django Rocks",
	"url":"http://www.djangorocks.com/", "views":20},
	{"title":"How to Tango with Django",
	"url":"http://www.tangowithdjango.com/", "views":30} ]

	other_pages = [
	{"title":"Bottle",
	"url":"http://bottlepy.org/docs/dev/", "views":1000},
	{"title":"Flask",
	"url":"http://flask.pocoo.org", "views":1500} ]
	
	cats = {"Python": {"pages": python_pages,"likes":128,"views":64},
	"Django": {"pages": django_pages,"likes":64,"views":32},
	"Other Frameworks": {"pages": other_pages,"likes":32,"views":16} }

	for cat, cat_data in cats.iteritems():
		c = add_cat(cat,cat_data["likes"],cat_data["views"])
	
		for p in cat_data["pages"]:
			add_page(c, p["title"], p["url"], p["views"])

	for c in category.objects.all():
		for p in page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views):
	p = page.objects.get_or_create(category=cat, title=title)[0]	
	p.url=url
	p.views=views
	p.save()
	return p
	
def add_cat(name,likes,views):
	c = category.objects.get_or_create(name=name)[0]
	c.likes = likes
	c.views = views
	c.save()
	return c			


if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()	