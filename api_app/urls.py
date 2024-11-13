from django.urls import path
from . views import *
urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('users-list', UsersList.as_view(), name="users-list"),
]
