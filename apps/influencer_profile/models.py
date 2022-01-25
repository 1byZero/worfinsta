# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class influencer_data(models.Model):
    influencer_user_name = models.CharField(max_length=100)
    influencer_id = models.PositiveIntegerField(max_length=100000000000)

class in