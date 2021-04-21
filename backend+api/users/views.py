from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UserCreateForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    model = get_user_model()
    template_name = 'registration/signup.html'
    success_message = 'Account created succesfully, You can Login now!'
    success_url = reverse_lazy('login')
