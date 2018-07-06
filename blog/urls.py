from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('singup/', views.SingIn.as_view()),
]