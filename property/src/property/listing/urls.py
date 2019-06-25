from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
    listing_development_create_view,
    listing_development_delete_view,
    listing_development_detail_view,
    listing_development_list_view,
    listing_development_update_view,
   
    )


app_name = 'listing'

urlpatterns = [
    path('development/<str:slug>/delete/', listing_development_delete_view),
    path('development/<str:slug>/edit/', listing_development_update_view),
    path('development/<str:slug>/', listing_development_detail_view),
     path('listing-new/', listing_development_create_view),
     path('listing-list/', listing_development_list_view),
    ]