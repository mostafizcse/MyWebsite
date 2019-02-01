from django import forms
from .models import  Contact, Post, Create_menu, Email_stor, Example, User, Requirments, slider, Team, Reviewlist, Events, Featurelist
from django.contrib.auth.forms import UserCreationForm



class teamForm(forms.ModelForm):
    class Meta:
        model=Team
        fields="__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class CreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=[

            'posttitle',
            'subtitle',
            'description'
        ]


class CreateEmailForm(forms.ModelForm):
    class Meta:
        model=Email_stor
        fields=[

            'email'

        ]

class CreateFormMenu(forms.ModelForm):
    class Meta:
        model=Create_menu
        fields=[
            'Example',
            'm_name',
            'm_title',
            'description'

        ]

class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]

class requermentForm(forms.ModelForm):
    class Meta:
        model=Requirments
        fields=[
            'job_title',
            'description',
        ]

class sliderForm(forms.ModelForm):
    class Meta:
        model=slider
        fields = "__all__"

class reviewlistForm(forms.ModelForm):
    class Meta:
        model=Reviewlist
        fields=[
            'name',
            'deciption',
        ]

class eventForm(forms.ModelForm):
    class Meta:
        model=Events
        fields=[
            'event',
            'location',
            'date'
        ]

class featurlistForm(forms.ModelForm):
    class Meta:
        model=Featurelist
        fields="__all__"