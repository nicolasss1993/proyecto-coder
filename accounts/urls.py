from django.urls import path
from django.contrib.auth import views
from accounts.views import registro_usuario, profile_view

urlpatterns = [
    path("login/", views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("register/", registro_usuario, name="register"),
    path(
        "logout/", views.LogoutView.as_view(next_page="hola"), name="logout"
    ),
    path("profile/", profile_view, name="profile")
]