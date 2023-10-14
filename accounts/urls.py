from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LDAPAuthenticationView

urlpatterns = [
    path("ldap-auth/", LDAPAuthenticationView.as_view(), name="ldap-auth"),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
