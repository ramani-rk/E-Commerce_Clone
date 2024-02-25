from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect #HR used for sending response #HR-redirect used for takeback the URL to the particular Page
from django.core.mail import send_mail # its used for sending the sending the mail
from django.contrib.auth import authenticate,login,logout #login & logout is used for user login & logout purpose
from django.contrib.auth.decorators import login_required # when user wants any changes after login, that time we must use login_required
from django.urls import reverse



def dummy(request):
    return render (request,'dummy.html')



def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

    

def registration(request):
    d={'usfo':UserForm(),'pfo':ProfileForm()}

# this condition is helps to check POST method and accept the image files.
    if request.method=='POST' and request.FILES:
        usfo=UserForm(request.POST)
        pfo=ProfileForm(request.POST,request.FILES)
        
# it checks userform & profileform valid or not
        if usfo.is_valid() and pfo.is_valid():
            NSUFO=usfo.save(commit=False)
            submittedPassword=usfo.cleaned_data['password'] #Cleaned_data is a dictionary, in that we store our data
            NSUFO.set_password(submittedPassword)
            NSUFO.save()
            NSPO=pfo.save(commit=False)
            NSPO.username=NSUFO
            NSPO.save()
            
            
            send_mail('registration',
                      'Successfully Registered your account in Amazon ',
                      'ramanikanthsasi@gmail.com',
                      [NSUFO.email],
                      fail_silently=False )
            return HttpResponse('Registration is Completed')        
    return render (request,'registration.html',d)



def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active: # is_active is used to check whether the user is an active user or not
                login(request,AUO)
                request.session['username']=username # Session means it stores user's data in a file for specific time
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Not a Active User')
        else:
            return HttpResponse('Invalid Details')
    return render(request,'user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('password was changed')
    return render(request,'change_password.html')

def reset_password(request):
    if request.method=='POST':
        password=request.POST['pw']
        username=request.POST['un']
        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(password)
            UO.save()
            return HttpResponse('reset_password is done')
        else:
            return HttpResponse('invalid data')
    return render(request,'reset_password.html')


@login_required
def display_details(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'display_details.html',d)


def mobiles(request):
    return render(request,'mobiles.html')


def electronics(request):
    return render(request,'electronics.html')
   
   
def today_deals(request):
    return render(request,'today_deals.html')


def amazon_mini_tv(request):
    return render(request,'amazon_mini_tv.html')


def homee(request):
    return render(request,'homee.html')


def webseries(request):
    return render(request,'webseries.html')


def short_films(request):
    return render(request,'short_films.html')


def comedy(request):
    return render(request,'comedy.html')
