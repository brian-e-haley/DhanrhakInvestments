from django.views.generic import ListView

from profiles.models import Quiz


class ProfileView(ListView):
    template_name = 'profiles/profile.html'
    model = Quiz
    context_object_name = 'quizzes'
    ordering = ['-pk']

    def get_queryset(self):
        return Quiz.objects.filter(teacher=self.request.user).all()
