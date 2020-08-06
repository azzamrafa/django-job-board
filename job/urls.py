from . import views
from django.urls import path, include

urlpatterns = [
   
    path('job_list', views.job_list),
    path('<int:id>', views.job_detail),
]
