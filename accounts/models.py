# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.

# class Profile(models.Model):
# 	user = models.ForeignKey(User)
# 	timeslot = models.DateTimeField(null=True, blank=True)
# 	section = models.ForeignKey(Section, null=True, blank=True)
# 	purpose = models.TextField(null=True, blank=True)

# 	def __str__(self):
# 		return self.timeslot, self.purpose, self.section

# 	def get_absolute_url(self):
# 		return reverse('accounts:account_detail', kwargs={'pk':self.pk})