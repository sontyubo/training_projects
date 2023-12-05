from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from .views import LoginView, RegisterView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]