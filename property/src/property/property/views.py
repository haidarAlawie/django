from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from listing.models import ListingPostDevelopment
def index_page(request):
	qs= ListingPostDevelopment.objects.all()[:5]
	context = {"title": "Home", "ListingPostDevelopment_list": qs}
	template_name= 'index.html'
	return render(request, template_name, context)


