from django.conf.urls import url

import views


urlpatterns =[

	url(r'^$', views.index, name='homeofrango'),
	url(r'about/', views.about, name='about'),

]