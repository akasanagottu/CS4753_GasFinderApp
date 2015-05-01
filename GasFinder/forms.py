__author__ = 'Apurva'

from django.contrib.auth.models import User
from django import forms
from GasFinder.models import Advertiser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    class Meta:
        model = User
        fields = ('username', 'password')

class AdvertiserForm(forms.ModelForm):
    tiers_choices = (
        ("Bronze", 'Bronze Tier: $1000 per month'),
        ("Silver", 'Silver Tier: $3000 per month'),
        ("Gold", 'Gold Tier: $5000 per month'),
        ("Platinum", 'Platinum Tier: $7000 per month'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Contact Email'}))
    tiers = forms.ChoiceField(choices=tiers_choices)
    class Meta:
        model = Advertiser
        fields = ('name', 'email', 'tiers')