from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User


class UserRegisterForm(UserCreationForm):
    ROLES = (('student', 'Student'), ('teacher', 'Teacher'))
    role = forms.ChoiceField(choices=ROLES)

    def save(self, commit=True):
        user = super().save()
        student = Group.objects.get(name='student')
        teacher = Group.objects.get(name='teacher')
        if self.cleaned_data['role'] == 'student':
            student.user_set.add(user)
        else:
            teacher.user_set.add(user)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2']
