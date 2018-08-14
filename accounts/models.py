from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class Profile(AbstractUser):
	ideal_weight = models.IntegerField(default=185)

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse('accounts:profile_detail', kwargs={'pk':pk})
	