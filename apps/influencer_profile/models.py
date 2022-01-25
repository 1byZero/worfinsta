# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class influencer_profile(models.Model):
    influencer_user_name = models.CharField(max_length=100)
    influencer_id = models.PositiveIntegerField()


class influencer_profile_data(models.Model):
    influencer_full_name = models.CharField(max_length=50)
    influencer_biography = models.CharField(max_length=500)
    influencer_followed = models.PositiveIntegerField()
    influencer_follow = models.PositiveIntegerField()
