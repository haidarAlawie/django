from django.http import HttpResponse
from django.shortcuts import render

def index_page(request):
	context = {"title": "Home"}
	template_name= 'index.html'
	return render(request, template_name, context)