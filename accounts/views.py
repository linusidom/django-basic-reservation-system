from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from accounts.models import Profile
from accounts.forms import ProfileForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class IndexTemplateView(TemplateView):
	template_name='accounts/index.html'

def signup(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.username = profile.email
			profile.save()
			return redirect('user_login')
	else:
		form = ProfileForm()
	return render(request, 'accounts/signup.html', {'form': form})

def update_profile(request, pk):
	if request.method == 'POST':
		form = ProfileUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.username = profile.email
			profile.save()
			messages.add_message(request, messages.INFO, 'Success, Profile Updated!')
			return redirect('accounts:profile_detail', pk=pk)
		else:
			return HttpResponse(form.errors)
	else:
		form = ProfileUpdateForm(instance=request.user)
	return render(request, 'accounts/profile_form.html', {'form': form})
class ProfileDetailView(LoginRequiredMixin, DetailView):
	model = Profile

	def get_queryset(self):
		user = self.request.user.pk
		queryset = Profile.objects.filter(pk=user)
		return queryset

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
	model = Profile
	success_url = reverse_lazy('index')