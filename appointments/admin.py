from django.contrib import admin
from appointments.models import Appointment, Counter, Section


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['counter','section', 'date', 'timeslot', 'patient_name']
    list_filter = ['counter', ]

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Counter)
admin.site.register(Section)
