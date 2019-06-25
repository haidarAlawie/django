from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import ListingPostDevelopment
from .forms import ListingDevelopmentModelForm

# def t(request):
# 	qs = ListingPostDevelopment.objects.all()
# 	template_name= 'listing/listing.html'
# 	context = {'object_list': qs}
# 	return render(request, template_name, context)

@login_required
def listing_development_create_view (request):
	form = ListingDevelopmentModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit= False)
		obj.user = request.user
		form.save()
		form = ListingDevelopmentModelForm()
	template_name= 'form.html'
	context = {'form': form }
	return render(request, template_name, context)


def listing_development_detail_view(request, slug):
	obj = get_object_or_404(ListingPostDevelopment, slug= slug)
	template_name= 'listing/development_detail.html'
	context = {'object': obj}
	return render(request, template_name, context)

def listing_development_list_view(request):
	qs = ListingPostDevelopment.objects.all()
	template_name= 'listing/development_list.html'
	context = {'object_list': qs, "title":"Listings"}
	return render(request, template_name, context)


def listing_development_update_view(request, slug):
	obj = get_object_or_404(ListingPostDevelopment, slug= slug)
	form = ListingDevelopmentModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		form= ListingDevelopmentModelForm()
	template_name= 'form.html'
	context = {'form': form, "title": f"Update{obj.title}"}
	return render(request, template_name, context)

def listing_development_delete_view(request, slug):
	obj = get_object_or_404(ListingPostDevelopment, slug= slug)
	if request.method == "POST":
		obj.delete()
		return redirect("/")
	template_name= 'listing/development_delete.html'
	context = {'object': obj}
	return render(request, template_name, context)
