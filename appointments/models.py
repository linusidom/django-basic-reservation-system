from django.db import models
from django.shortcuts import reverse
from accounts.models import Profile

class Appointment(models.Model):
	
	# TIMESLOT = (
	# 	(0, '08:00 - 09:00'),
	# 	(1, '09:00 - 10:00'),
	# 	(2, '10:00 - 11:00'),
	# 	(3, '11:00 - 12:00'),
	# 	(4, '12:00 - 13:00'),
	# 	(5, '13:00 - 14:00'),
	# 	(6, '14:00 - 15:00'),
	# 	(7, '15:00 - 16:00'),
	# 	(8, '16:00 - 17:00')
	# 	)
	TIMESLOT = (
		(0, '09:00 - 10:00'),
		(1, '10:00 - 11:00'),
		(2, '11:00 - 12:00'),
		(3, '12:00 - 13:00'),
		(4, '13:00 - 14:00'),
		(5, '14:00 - 15:00'),
		(6, '15:00 - 16:00'),
		(7, '16:00 - 17:00'),
		(8, '17:00 - 18:00'),
		)

	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	section = models.ForeignKey('Section',null=True, blank=True)
	counter = models.ForeignKey('Counter',null=True, blank=True)
	date = models.DateField(null=True, blank=True)
	timeslot = models.IntegerField(choices=TIMESLOT,null=True, blank=True)
	purpose = models.CharField(max_length = 100,null=True, blank=True)
	document = models.FileField(upload_to='static/css', null=True, blank=True)
	
	def __str__(self):
		return '{} {} {} {} {}'.format(self.user, 
									self.section, 
									self.date,
									self.time,
									self.purpose)

	@property
	def time(self):
		return self.TIMESLOT[self.timeslot][1]

	def get_absolute_url(self):
		return reverse('appointments:appointment_detail', kwargs={'pk':self.pk})

	class Meta:
		unique_together = ('section','counter','date', 'timeslot')

class Counter(models.Model):
	section = models.ForeignKey('Section',null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=100,null=True, blank=True)

	def __str__(self):
		return self.name	

class Section(models.Model):
	section_name = models.CharField(max_length=100,null=True, blank=True)

	def __str__(self):
		return self.section_name










