from django.urls import path

from profiles import views as profile_views

urlpatterns = [
    path('', profile_views.ProfileView.as_view(), name='profile'),
    path('quiz/new/',
         profile_views.QuizCreateView.as_view(),
         name='quiz_create'),
    path('quiz/<int:pk>/',
         profile_views.QuizDetailView.as_view(),
         name='quiz_detail'),
    path('quiz/<int:quiz>/question/mc/create',
         profile_views.McQuestionCreateView.as_view(),
         name='mc_question_create'),
    path('quiz/<int:quiz>/question/sa/create',
         profile_views.SaQuestionCreateView.as_view(),
         name='sa_question_create'),
    path('quiz/<int:quiz>/question/<int:pk>',
         profile_views.QuestionDetailView.as_view(),
         name='question_detail'),
]
