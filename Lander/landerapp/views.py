from django.shortcuts import render
from landerapp.forms import UserForm
from landerapp.forms import UserProfileInfo

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'landerapp/index.html')
def sign_up(request):
    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save(commit=False)
            user.username=user.email.split('@')[0].title()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()
            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfo()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'landerapp/landersignup.html',{'profile_form':profile_form})

def log_in(req):
    if req.method=='POST':
        email=req.POST.get('email')
        password=req.POST.get('password')
        username=email.split('@')[0].title()
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(req,user)
                return HttpResponseRedirect(reverse('index'))
                logged_in=True
            else:
                return HttpResponse("Your account seems to be inactive")
        else:
            print("Someone tried to login and failed")
            return HttpResponse("Invalid login credentials")
    else:
        logged_in=False
        return render(req,'landerapp/landerlog.html',{'logged_in':logged_in})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))
