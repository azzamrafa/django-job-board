from . import views
from django.urls import path, include


app_name = 'job'

urlpatterns = [
   
    path('job_list', views.job_list),
    path('<str:slug>', views.job_detail, name='job_detail'),
]
