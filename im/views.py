from django.shortcuts import render
from django.views.generic import FormView, TemplateView, ListView, DetailView

from im.models import Ticket
from .forms import CustomUserCreationForm, NewTicketForm
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

class NewTicketView(FormView):
    form_class = NewTicketForm
    template_name = "im/new_ticket.html"
    success_url = "/exito"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class TicketListView(ListView):
    template_name = "im/tickets.html"
    model = Ticket
    context_object_name = "tickets"

class TicketDetail(DetailView):
    template_name = "im/ticket_detail.html"
    model = Ticket