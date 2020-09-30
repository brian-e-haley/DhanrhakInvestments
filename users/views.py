from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView

from users import forms as user_forms


class CreateUserView(CreateView):
    """View to register users."""
    model = User
    form_class = user_forms.UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('login')  # TODO swap to profile route
