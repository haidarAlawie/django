from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from .forms import SignUpForm


class UserView(DetailView):
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #send_mail(subject, message, from_mail, to_list, fail_silently=True)
            subject = 'thank you for signing up'
            message= 'welcome to hq properties./n we will be intouch soon'
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER, 'haidar.alawie@hotmail.co.uk']
            send_mail(subject,message,from_email,to_list,fail_silently=True)

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})