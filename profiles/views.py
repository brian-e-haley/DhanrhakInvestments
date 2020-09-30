from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from profiles.models import Quiz


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'profiles/profile.html'
    model = Quiz
    context_object_name = 'quizzes'

    def get_queryset(self):
        return Quiz.objects.filter(teacher=self.request.user).all()


class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'description']
    context_object_name = 'quiz'

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)


class QuizDetailView(LoginRequiredMixin, DetailView):
    model = Quiz
