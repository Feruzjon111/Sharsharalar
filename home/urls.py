from django.urls import path
from . import views

urlpatterns = [
    path('', views.bosh_sahifa, name='bosh_sahifa'),
    path('sharsharalar/', views.sharshara_royxati, name='sharshara_royxati'),
    path('sharshara/<int:pk>/', views.sharshara_detali, name='sharshara_detali'),
]
