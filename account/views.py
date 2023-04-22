from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import UserApi
from django.contrib import messages
from watermark.utils import get_data
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

@login_required
def api(request):
    try:
        user_api  = UserApi.objects.get(user=request.user)
    except Exception:
        return redirect('home')
    return render(request,'account/api.html',{'user_data':user_api,'api':True})

@csrf_exempt
def watermark_image(request):
    code = 404
    if request.method == 'POST':
        user = request.POST.get('username')
        try:
            user = User.objects.get(username=user)
            key = request.POST.get('key')
            is_exist = UserApi.objects.filter(user=user,api_key=key).exists()
            if is_exist:
                data = get_data(request)
                code = 200
            else:
                raise Exception('not valid')

        except Exception:
            data = {'message':'invalid user or api key'}
    else :
        data = {'message':'invalid request type'}
    data = json.dumps(data)
    return HttpResponse(data,status=code)
        
        
        

def sign_in(request):
    email = False
    if request.method == "POST":
        email = request.POST.get('emailInput')
        password = request.POST.get('password')
        
        user = authenticate(username=email,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request, "Signed In Successfull !")
            return redirect('home')
        else:
            messages.error(request, "Enter valid credentials !")
            
    return render(request,'account/signIn.html',{'email':email,'sign_in':True})

def sign_up(request):
    if request.method == "POST":
        email = request.POST.get('emailInput')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if email_obj := User.objects.filter(username=email).exists():
            messages.error(request, "User already exist!")
        elif password1 == password2:
            user = User.objects.create_user(username=email,password=password1)
            user.save()
            user_api = UserApi.objects.create(user=user)
            user_api.save()
            messages.success(request, "User Created Successfully !")
            return redirect('sign_in')
        else:
            messages.error(request, "Password must be same!")

    return render(request,'account/signUp.html',{'sign_up':True})
        

def sign_out(request):
    logout(request)
    return redirect('home')