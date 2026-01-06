from django.urls import path
from .views import UserRegistrationView,UserlLoginView,UserProfileView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserlLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
]