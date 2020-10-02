from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, ListView
from extra_views import CreateWithInlinesView, InlineFormSetFactory

from profiles.models import Option, Question, Quiz


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


class OptionInline(InlineFormSetFactory):
    model = Option
    fields = ['text', 'correct']
    factory_kwargs = {'extra': 1,
                      'can_delete': False}


class SaQuestionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Question
    fields = ['question']
    context_object_name = 'question'
    template_name = 'profiles/question_sa_form.html'

    def get_quiz(self):
        """
        Method to return the parent quiz of this view.
        :return: Quiz
        """
        quiz = Quiz.objects.get(pk=self.kwargs['quiz'])
        return quiz

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quiz'] = self.get_quiz()
        return context

    def form_valid(self, form):
        form.instance.quiz = self.get_quiz()
        form.instance.category = 'sa'
        return super().form_valid(form)

    def test_func(self):
        teacher = self.request.user.groups.first().name == 'teacher'
        quiz_creator = self.request.user == \
                       self.get_quiz().teacher
        return teacher and quiz_creator


class McQuestionCreateView(LoginRequiredMixin,
                           UserPassesTestMixin,
                           CreateWithInlinesView):
    model = Question
    inlines = [OptionInline]
    fields = ['question']
    context_object_name = 'question'
    template_name = 'profiles/question_mc_form.html'

    def get_quiz(self):
        """
        Method to return the parent quiz of this view.
        :return: Quiz
        """
        quiz = Quiz.objects.get(pk=self.kwargs['quiz'])
        return quiz

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quiz'] = self.get_quiz()
        return context

    def form_valid(self, form):
        form.instance.quiz = self.get_quiz()
        form.instance.category = 'mc'
        return super().form_valid(form)

    def test_func(self):
        teacher = self.request.user.groups.first().name == 'teacher'
        quiz_creator = self.request.user == \
                       self.get_quiz().teacher
        return teacher and quiz_creator


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
