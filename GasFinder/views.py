__author__ = 'Apurva'

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from GasFinder.models import Advertiser, Station
from GasFinder.forms import UserForm, AdvertiserForm

@login_required
def home(request):
    return render(request,'Home.html')

@login_required
def search(request):
    if request.method == 'POST':
        #station = Station(address = request.POST["currLoc"], octane87 = request.POST["87oct"], octane89 = request.POST["89oct"], octane92 = request.POST["92oct"])
        #station.save()
        address = "'"+ request.POST["currLoc"] +"'"
        addresses = []

        if "87oct" in request.POST:
            is87 = True
        else:
            is87 = False
        if "89oct" in request.POST:
            is89 = True
        else:
            is89 = False
        if "92oct" in request.POST:
            is92 = True
        else:
            is92 = False

        print(is87)
        print(is89)
        print(is92)

        stations = Station.objects.all()
        for x in stations:
            addresses.append("'" + x.address + "'")
        return render(request, 'Search.html', {"pastAddress": address, 'stations': stations, 'stationAddresses': addresses, 'is87':is87, 'is89':is89, 'is92': is92 })
    return render(request, 'Search.html')

@login_required
def search_local(request):
    return render(request, 'SearchLocal.html')

@login_required
def submit_price(request):
    if request.method == 'POST':
        station = Station(address = request.POST["currLoc"], octane87 = request.POST["87oct"], octane89 = request.POST["89oct"], octane92 = request.POST["92oct"])
        station.save()
        address = "'"+ request.POST["currLoc"] +"'"
        return render(request, 'SubmitPrice.html', {"pastAddress": address})
    return render(request, 'SubmitPrice.html')

@login_required
def forgot_account(request):
    return render(request, 'ForgotAccountInformation.html')

def advertise(request):

    # Like before, get the request's context.
    context = RequestContext(request)
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    submitted = False

    goldList = Advertiser.objects.filter(tiers="Gold")
    silverList= Advertiser.objects.filter(tiers="Silver")
    bronzeList = Advertiser.objects.filter(tiers="Bronze")
    platList = Advertiser.objects.filter(tiers="Platinum")

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        advertiser_form = AdvertiserForm(data=request.POST)
        # If the two forms are valid...
        if advertiser_form.is_valid():
            # Save the user's form data to the database.
            advertiser = advertiser_form.save()

            # Update our variable to tell the template registration was successful.
            submitted = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print advertiser_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        advertiser_form = AdvertiserForm()

    # Render the template depending on the context.
    return render_to_response(
            'Advertise.html',
            {'advertiser_form': advertiser_form, 'submitted': submitted, 'platList': platList, 'goldList': goldList, 'silverList': silverList, 'bronzeList': bronzeList},
            context)

@login_required
def account(request):
    context = RequestContext(request)
    if request.method == 'POST':
        s = request.user
        if s.check_password(request.POST['CurrentPassword']):
            s.set_password(request.POST['NewPassword'])
            s.save()
            return render_to_response('MainPage.html', {'message': 'Your password has been successfully changed. Please login again.'}, context)

        return render_to_response('Account.html', {'message': 'Your password was not able to be changed. Please try again.'}, context)
    else:
        return render_to_response('Account.html', {"message": ''}, context)

def about(request):
    return render(request, 'About.html')

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

def user_login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return render_to_response('MainPage.html', {"message": 'Your SecureWitness account is disabled.'}, context)
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response('MainPage.html', {"message": 'Invalid login details supplied' }, context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('MainPage.html', {"message": ''}, context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()


            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'Register.html',
            {'user_form': user_form, 'registered': registered},
            context)