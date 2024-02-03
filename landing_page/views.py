from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'landing_page/index.html')


def privacy_policy(request):
    return render(request, 'landing_page/privacy-policy.html')


def cancelatio_policy(request):
    return render(request, 'landing_page/cancelation-policy.html')
