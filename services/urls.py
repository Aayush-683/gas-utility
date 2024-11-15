from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('detail/<int:pk>/', views.request_detail, name='request_detail'),
    path('register/', views.register, name='register'),
    path('support/', views.support_dashboard, name='support_dashboard'),
    path('support/update/<int:pk>/', views.update_request_status, name='update_request_status'),
]