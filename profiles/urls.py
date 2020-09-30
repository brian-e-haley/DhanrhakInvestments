from django.urls import path

from profiles import views as profile_views

urlpatterns = [
    path('', profile_views.ProfileView.as_view(), name='profile'),
    path('quiz/new/',
         profile_views.QuizCreateView.as_view(),
         name='quiz_create'),
]
