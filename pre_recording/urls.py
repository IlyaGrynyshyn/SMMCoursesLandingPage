from django.contrib import admin
from django.urls import path, include
from pre_recording.views import pre_recording,save_form

urlpatterns = [
    path('', pre_recording),
    path('ajax-form/', save_form, name='save_form')

]