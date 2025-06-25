from django.urls import path

from .views import AdminRegisterView, EmailLoginView, CustomTokenRefreshView

urlpatterns = [
    path("api/login/", EmailLoginView.as_view(), name="api_login"),  # renamed from /token/
    path("api/refresh/", CustomTokenRefreshView.as_view(), name="api_token_refresh"),  # renamed
    path("api/register/", AdminRegisterView.as_view(), name="api_admin_register"),  # renamed
]
