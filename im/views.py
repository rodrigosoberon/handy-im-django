from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = "im/register.html"
    success_url = "/exito"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LandingView(TemplateView):
    template_name = "im/landing.html"

class DashboardView(TemplateView):
    template_name = "im/dashboard.html"

class ExitoView(TemplateView):
    template_name = "im/exito.html"