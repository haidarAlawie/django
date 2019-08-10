from django.shortcuts import render
from .models import SearchQuery
from listing.models import ListingPostDevelopment

def search_view(request):
	query= request.GET.get("q", None)
	template_name= 'searches/view.html'
	user = None
	context= {"query": query}
	if request.user.is_authenticated:
		print(request.user)
		
		context= {"query": query}
		print(query)
	if query is not None:
		print("there is a query")
		SearchQuery.objects.create(user=user, query=query)
		object_list = ListingPostDevelopment.objects.search(query=query)
		context['object_list'] = object_list
	return render(request, template_name, context)

def listing_development_detail_view(request, slug):
	obj = get_object_or_404(ListingPostDevelopment, slug= slug)
	template_name= 'searches/development_detail.html'
	context = {'object': obj}
	return render(request, template_name, context)