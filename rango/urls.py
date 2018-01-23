from django.conf.urls import url

import views


urlpatterns =[

	url(r'^$', views.index, name='homeofrango'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_category/$', views.add_category, name='addcategory'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
views.show_category, name='show_category'),

]