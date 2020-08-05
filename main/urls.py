from django.urls import path
from main import views

urlpatterns=[
    path('/input',views.homepage,name="homepage"),
    path('/output',views.output,name="output"),
    
]