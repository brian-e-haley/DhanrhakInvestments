from django.contrib.auth import views as auth_views
from django.urls import path

from users import views as user_views

urlpatterns = [
    path('register/',
         user_views.CreateUserView.as_view(),
         name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
]
