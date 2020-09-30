from django.urls import path

from profiles import views as profile_views

urlpatterns = [
    path('', profile_views.ProfileView.as_view(), name='profile'),
]
