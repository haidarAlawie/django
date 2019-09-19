from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    age = forms.CharField(label='Age', max_length=100)