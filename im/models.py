from unicodedata import category
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    # Custom user model manager where email is the unique identifiers for authentication instead of usernames.

    def create_user(self, email, password, **extra_fields):

        # Create and save a User with the given email and password.

        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        # Create and save a SuperUser with the given email and password.

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Message(models.Model):
    title = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET('DELETED'))
    text = models.CharField(max_length=500)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Team(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(CustomUser)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class TicketStatus(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Ticket status")
        verbose_name_plural = _("Ticket states")


class Priority(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Priority")
        verbose_name_plural = _("Priorities")


class Log(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)

    def entry_display(self):
        return f"{self.created} - {self.description}"

    def __str__(self):
        return self.entry_display()


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    ticket_status = models.ForeignKey(
        TicketStatus, on_delete=models.SET('DELETED'))
    priority = models.ForeignKey(Priority, on_delete=models.SET('DELETED'))
    category = models.ForeignKey(
        Category, on_delete=models.SET('DELETED'), null=True)
    assigned = models.ForeignKey(
        CustomUser, on_delete=models.SET('DELETED'), null=True)
    team = models.ForeignKey(Team, on_delete=models.SET('DELETED'), null=True)
    messages = models.ManyToManyField(Message)
    logs = models.ManyToManyField(Log)

# TODO crear modelos para Tests y Problemas
