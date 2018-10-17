from django.conf.urls import url
from model1 import views

urlpatterns =[
    url(r'web/',views.home,name='home'),
]