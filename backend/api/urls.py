from django.urls import path

from . import views

urlpatterns=[
    path('', views.api_homeget),
    path('post/', views.api_homepost),
]