from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import UserRegisterForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'users/index.html'

class SignInView(TemplateView):
    template_name = 'users/sign_in.html'

class SignUpView(CreateView):
    template_name = 'users/sign_up.html'
    form_class = UserRegisterForm