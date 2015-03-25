__author__ = 'Apurva'

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    return render(request, 'Home.html')


def register(request):
    return render(request, 'Register.html')


def search(request):
    return render(request, 'Search.html')


def search_local(request):
    return render(request, 'SearchLocal.html')


def submit_price(request):
    return render(request, 'SubmitPrice.html')


def main_page(request):
    return render(request, 'MainPage.html')


def forgot_account(request):
    return render(request, 'ForgotAccountInformation.html')

def advertise(request):
    return render(request, 'Advertise.html')

def account(request):
    return render(request, 'Account.html')

def about(request):
    return render(request, 'About.html')