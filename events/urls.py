from . import views
from django.urls import path

urlpatterns = [
    path('', views.events.as_view(), name='events'),
    path('<slug:slug>/', views.events_detail.as_view(), name='events_detail'),
]
