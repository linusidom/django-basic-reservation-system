from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from appointments.forms import AppointmentForm
from appointments.models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.core.urlresolvers import reverse_lazy
import datetime
from django.views.generic import (TemplateView, ListView, DetailView,
								CreateView, UpdateView, DeleteView)


@login_required
def new_appointment(request):
	date = datetime.date.today()
	appointment_account = Appointment.objects.filter(user=request.user, date=date)
	print(appointment_account)
	if request.method == 'POST':
		form = AppointmentForm(request.POST)
		if form.is_valid():
			appointment = form.save(commit=False)
			appointment.user = request.user
			appointment.save()
			return redirect('/')
	else:
		form = AppointmentForm()
	return render(request, 'appointments/appointment_form.html', {'form': form})

class AppointmentListView(LoginRequiredMixin, ListView):
	model = Appointment

	def get_queryset(self):
		user = self.request.user
		queryset = Appointment.objects.filter(user=user)
		return queryset


class AppointmentDetailView(LoginRequiredMixin, DetailView):
	model = Appointment

	def get_queryset(self):
		user = self.request.user
		queryset = Appointment.objects.filter(user=user)
		return queryset

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
	model = Appointment
	form_class = AppointmentForm

class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
	model = Appointment
	success_url = reverse_lazy('index')






