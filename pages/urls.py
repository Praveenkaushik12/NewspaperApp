from django.urls import path
from .views import HomePageView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('users/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
]
