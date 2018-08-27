from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserAccountInfo,UAExtraInfo,postform
from django.urls import reverse
from .models import DataModel
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'Index.html')

def SignUp(request):
    registered = False
    if request.method == 'POST':
        user_form = UserAccountInfo(data=request.POST)
        profile_form = UAExtraInfo(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'Profile_Pic' in request.FILES:
                profile.Profile_Pic = request.FILES['Profile_Pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserAccountInfo()
        profile_form = UAExtraInfo()
    return render(request,'Signup.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})

def postmedata(request):
    register = False
    if request.method == 'POST':
        datasmodel = postform(data=request.POST)
        if datasmodel.is_valid():
            dallas = datasmodel.save(commit=False)
            if 'Select_Your_Image' in request.FILES:
                dallas.Select_Your_Image = request.FILES['Select_Your_Image']
            dallas = datasmodel.save()

            register = True
        else:
            return HttpResponse("Error")
    else:
        datasmodel = postform()
    return render(request,'posthere.html',{'datasmodel':datasmodel,'register':register})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('AppBasic:Home'))
            else:
                return HttpResponse("Account is not active")
        else:
            print("Some body tried to login with wrong credentials")
            return HttpResponse("There is no account with this credentials.")
    else:
        return render(request,'login.html',{})

@login_required
def LogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('AppBasic:Home'))



def contribute(request):
    contrib_object = DataModel.objects.all()
    mydict = {'contrib_object':contrib_object}
    return render(request,'Contributions.html',context = mydict)




