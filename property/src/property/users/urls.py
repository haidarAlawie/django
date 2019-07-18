from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import UserView, signup

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('profile/',  login_required(UserView.as_view()), name='profile'),
    path('signup/', signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),   
    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        # auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete')

    # path('password_reset/',auth_views.password_reset, name='password_reset'),
    # path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # path('reset/(<uidb64>/(<token>)/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete')




]