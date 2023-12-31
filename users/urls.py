from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login", views.UserLogIn.as_view()),
    path("logout", views.UserLogOut.as_view()),
    path("signin", views.UserSignIn.as_view()),
    path("me", views.MyProfile.as_view()),
    path("@<str:username>", views.PublicUserProfile.as_view()),
    path("change-password", views.ChangeUserPassword.as_view()),
    path("token-login", obtain_auth_token),
    path("jwt-login", views.JWTLogin.as_view()),
]