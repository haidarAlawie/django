from django import forms
from .models import ListingPostDevelopment
class ListingDevelopmentForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	description = forms.CharField(widget=forms.Textarea)
	first_line_address = forms.CharField()
	second_line_address = forms.CharField()
	postcode = forms.CharField()
	number_of_properties= forms.IntegerField()
	site_plan = forms.IntegerField()
	price = forms.DecimalField()
	rent = forms.DecimalField()
	ownership = forms.CharField()	
	tenure  = forms.CharField() 


class ListingDevelopmentModelForm(forms.ModelForm):
	class Meta:
		model = ListingPostDevelopment
		fields =[
		'title',
		'image',
		'slug',
		'description', 
		'first_line_address' ,
		'second_line_address',
		'postcode',
		'number_of_properties',
		'site_plan',
		'price',
		'rent',
		'ownership',
		'tenure',
		'dropdown',
		]
	def clean_title(self, *args, **kwargs):
		instance = self.instance
		title = self.cleaned_data.get('title')
		qs = ListingPostDevelopment.objects.filter(title__iexact=title)
		if instance is not None:
			qs = qs.exclude(pk = instance.pk)
		if qs.exists():
			raise forms.ValidationError("This title has already been used- use another which has not")
		return title


	def clean_price(self, *args, **kwargs):
		price = self.cleaned_data.get("price")
		if price < 500:
			raise forms.ValidationError("Too cheap")
		return price