from django.shortcuts import render
from .models import SearchQuery
from listing.models import ListingPostDevelopment

def search_view(request):
	query= request.GET.get("q", None)
	template_name= 'searches/view.html'
	user = None
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