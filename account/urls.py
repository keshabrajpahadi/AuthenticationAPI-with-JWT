from django.urls import path
from .views import UserRegistrationView,UserlLoginView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserlLoginView.as_view(),name='login'),
]