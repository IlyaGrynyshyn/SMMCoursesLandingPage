from django.http import JsonResponse
from django.shortcuts import render
from .models import Pre_Registration
from django.utils import timezone


def pre_recording(request):
    return render(request, 'pre_recording/index.html')


def save_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        if not name:
            print('No name')
        else:
            pre_registration = Pre_Registration(name=name, phone=phone, email=email)
            pre_registration.save()
        return JsonResponse({'status': 'OK'})
    else:
        return JsonResponse({'status': 'error`'})
