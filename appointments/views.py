from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from appointments.forms import AppointmentForm
from appointments.models import Appointment, Counter, Section
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.core.urlresolvers import reverse_lazy
import datetime
from django.views.generic import (TemplateView, ListView, DetailView,
								CreateView, UpdateView, DeleteView)


# @login_required
# def new_appointment(request):
# 	if request.method == 'POST':
# 		form = AppointmentForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			appointment = form.save(commit=False)
# 			appointment.user = request.user
# 			appointment.save()
# 			return redirect('appointments:appointment_list')
# 	else:
# 		form = AppointmentForm()
# 	return render(request, 'appointments/appointment_form.html', {'form': form})

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

class AppointmentCreateView(LoginRequiredMixin, CreateView):
	model = Appointment
	form_class = AppointmentForm
	success_url = reverse_lazy('appointments:appointment_list')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AppointmentCreateView, self).form_valid(form)

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
	model = Appointment
	form_class = AppointmentForm

class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
	model = Appointment
	success_url = reverse_lazy('appointments:appointment_list')






