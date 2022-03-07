from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.LandingView.as_view()),
    path("register", views.RegisterView.as_view(), name='register'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("exito",views.ExitoView.as_view()),
    path("dashboard", views.DashboardView.as_view()),
]