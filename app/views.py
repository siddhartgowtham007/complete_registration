from django.shortcuts import render
from  app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def registration(request):
    ufo=userforms()
    pfo=profileforms()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=userforms(request.POST)
        pfd=profileforms(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFO.set_password(pw)
            MUFO.save()

            MUPO=pfd.save(commit=False)
            MUPO.username=MUFO
            MUPO.save()
            send_mail('registration','thank u for registration',
                      'yanaganigowtham1432@gmail.com',[User.email],fail_silently=True)

            return HttpResponse('registration successful')
        
        
    return render(request,'registration.html',d)




def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home_page'))
        else:
            return HttpResponse('invalid credentitals')
        
    return render(request,'user_login.html')


def home_page(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home_page.html',d)
    return render(request,'home_page.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_page'))


@login_required
def profile_display(request):
    un=request.session.get('username')
    UO=User.objects.get(username=un)
    PO=profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}

    return render(request,'profile_display.html',d)


@login_required
def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('Password changed Successfully')
    return render(request,'change_password.html')



def reset_password(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']

        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(password)
            UO.save()
            return HttpResponse('reset is done')
        else:
            return HttpResponse('U r Username is not in our DataBase')

    return render(request,'reset_password.html')