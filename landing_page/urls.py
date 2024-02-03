from django.contrib import admin
from django.urls import path, include
from landing_page.views import index, privacy_policy, cancelatio_policy

urlpatterns = [
    path('', index, name='landing_page'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('cancelation_policy/', cancelatio_policy, name='cancelation_policy')

]
