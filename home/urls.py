from django.urls import path

from home import views as home_views

urlpatterns = [
    path('', home_views.HomeView.as_view(), name='home')
]
