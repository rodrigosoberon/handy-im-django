from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import Ticket

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserAuthenticationForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['messages', 'logs']