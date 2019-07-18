from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import search_view


urlpatterns = [
	path('', search_view),
	]
