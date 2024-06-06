from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('update-profile/', views.update_profile, name="update-profile")
]
