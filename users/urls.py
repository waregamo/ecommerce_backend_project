from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # List all users (optional)
    path("", views.UserListView.as_view(), name="user-list"),

    # Register new user
    path("register/", views.RegisterView.as_view(), name="register"),

    # JWT Authentication
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
