from django import forms
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(UserCreationForm):
	class Meta():
		model = Profile
		fields = ['email','password1','password2','ideal_weight']

class ProfileUpdateForm(forms.ModelForm):
	class Meta():
		model = Profile
		fields = ['email','ideal_weight']