from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'demo',views.fun,name='fun'),
]