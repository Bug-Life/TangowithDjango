from django.conf.urls import url
import views


urlpatterns =[

	url(r'^$', views.index, name='homeofrango'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_category/$', views.add_category, name='addcategory'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
views.show_category, name='show_category'),

]
