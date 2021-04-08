from . import views
from django.urls import path

urlpatterns = [
    path('', views.events, name='events'),
    path('<slug:slug>/', views.events_detail, name='events_detail'),
]
