from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	#Above uses from the default user model of Django.

	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return self.user.username

class category(models.Model):

	name = models.CharField(max_length=128, unique=True)
	likes = models.IntegerField(default=0)
	views = models.IntegerField(default=0)
	slug = models.SlugField(unique= True)

	#overriding save method to store the slugged version of category.
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(category, self).save(*args, **kwargs)


	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name
	

class page(models.Model):
	
	category = models.ForeignKey(category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __str__(self): 
		return self.title

	def __unicode__(self):
		return self.title
