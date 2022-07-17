# Create your models here.
from django.db import models


class influencer_profile(models.Model):
    influencer_user_name = models.CharField(max_length=100)
    influencer_id = models.PositiveIntegerField()


class influencer_profile_data(models.Model):
    influencer_full_name = models.CharField(max_length=70)
    influencer_biography = models.CharField(max_length=70)
    influencer_followed = models.BigIntegerField()
    influencer_follow = models.BigIntegerField()
