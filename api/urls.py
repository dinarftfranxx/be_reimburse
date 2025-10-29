#api/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView

urlpatterns = [
    # Ini memberitahu Django, "Jika sisa URL-nya adalah 'login/',
    # jalankan fungsi 'obtain_auth_token'"
    path('login/', obtain_auth_token, name='api_login'),
    path('createUser/', RegisterView.as_view(), name='api_create_user'),
]

