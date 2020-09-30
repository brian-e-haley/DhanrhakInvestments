from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from profiles.models import Quiz


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'profiles/profile.html'
    model = Quiz
    context_object_name = 'quizzes'
    ordering = ['-pk']

    def get_queryset(self):
        return Quiz.objects.filter(teacher=self.request.user).all()


class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
