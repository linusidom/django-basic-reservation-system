from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    """Contains info about appointment"""

    TIMESLOT_LIST = (
        (0, '09:00 – 10:00'),
        (1, '10:00 – 11:00'),
        (2, '11:00 – 12:00'),
        (3, '12:00 – 13:00'),
        (4, '13:00 – 14:00'),
        (5, '14:00 – 15:00'),
        (6, '15:00 – 16:00'),
        (7, '16:00 – 17:00'),
        (8, '17:00 – 18:00'),
    )
    
    user = models.ForeignKey(User)
    section = models.ForeignKey('Section', null=True, blank=True)
    counter = models.ForeignKey('Counter', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    patient_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.time, self.counter, self.patient_name)

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]

    class Meta:
        unique_together = ('section','counter', 'date', 'timeslot')

   


class Counter(models.Model):
    """Stores info about doctor"""
    section = models.ForeignKey('Section', null=True, blank=True)
    counter_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.counter_name

class Section(models.Model):
    section_name = models.CharField(max_length = 100, null=True, blank=True)

    def __str__(self):
        return self.section_name