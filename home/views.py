from django.shortcuts import render,redirect
from watermark.utils import get_data
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from . models import ImageModel
    

def home(request):
    if request.method != 'POST':
        return render(request,'home/index.html',{'home':True})
    # try:
    paths = get_data(request)
    data = json.dumps({'status':200,'paths':paths})

    # except Exception:
        # data = json.dumps({'status':404})
    return JsonResponse(data,safe=False)

@login_required
def history(request):
    image_models = ImageModel.objects.filter(user=request.user)
    return render(request,'home/history.html',{'images':image_models,'history':True})
