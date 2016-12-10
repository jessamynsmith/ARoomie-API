from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from aroomieapp.constants import *

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')
    dob = models.DateField()
    gender = models.CharField(max_length = 6)
    race = models.IntegerField(choices = RACE_CHOICES)
    phone = models.CharField(max_length = 10) #Consider +60 as default
    lifestyle_info = models.CharField(max_length = 500)
    gender_pref = models.IntegerField(choices = GENDER_CHOICES)
    race_pref = models.IntegerField(choices = RACE_CHOICES)
    budget_pref = models.IntegerField(default = 0)
    move_in_pref = models.DateField()
    avatar = models.ImageField(upload_to = 'user/avatar/', blank = False)

    def __str__(self):
        return self.user.get_full_name()

class Advertisement(models.Model):

    rental = models.IntegerField(default = 0)
    move_in = models.DateField()
    deposit = models.IntegerField(default = 0)
    amenity = models.CharField(max_length = 500)
    rule = models.CharField(max_length = 500)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    gender_pref = models.IntegerField(choices = GENDER_CHOICES)
    race_pref = models.IntegerField(choices = RACE_CHOICES)
    photo = models.ImageField(upload_to = 'advertisement/photo/', blank = False)
    created_at = models.DateTimeField(default = timezone.now)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'advertisement')

    def __str__(self):
        return self.created_by.get_full_name()

class Rating(models.Model):
    score = models.IntegerField()
    rated_at = models.DateTimeField(default = timezone.now)
    rated_by = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'rater')
    rated_to = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'target')

    def __str__(self):
        return self.rated_to.get_full_name()

class Message(models.Model):
    content = models.CharField(max_length = 500)
    sent_at = models.DateTimeField(default = timezone.now)
    sent_by = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'sender')
    sent_to = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'recipient')

    def __str__(self):
        return self.sent_to.get_full_name()
