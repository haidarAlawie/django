from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class ListingPostDevelopment(models.Model):
	user = models.ForeignKey(User, default =1,null = True, on_delete= models.SET_NULL)
	image = models.ImageField(upload_to='image/', blank=True, null=True)
	title = models.CharField(max_length= 120 )
	slug = models.SlugField(unique=True)
	description = models.TextField(null= True )
	first_line_address = models.CharField(null= True ,max_length=50)
	second_line_address = models.CharField(null= True ,max_length=50, blank = True)
	postcode = models.CharField(null= True,max_length=12)
	number_of_properties= models.IntegerField(null= True )
	site_plan = models.IntegerField(null= True )
	price = models.DecimalField(null= True ,max_digits=10, decimal_places=2)
	rent = models.DecimalField(null= True ,max_digits=10, decimal_places=2)
	ownership = models.CharField(null= True ,max_length=50)
	tenure  = models.CharField(null= True ,unique=True,max_length=50) 

	def get_absolute_development_url(self):
		return f"/listing/development/{self.slug}"

	def get_edit_development_url(self):
		return f"/listing/development/{self.slug}edit"


	def get_delete_development_url(self):
		return f"/listing/development/{self.slug}/delete"