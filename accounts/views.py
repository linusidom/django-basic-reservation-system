# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, DetailView,
                                CreateView, UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class SignUpCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:user_login')

class AccountDetailView(LoginRequiredMixin, DetailView):
    login_url = 'accounts:user_login'
    model = User
    template_name = 'accounts/account_detail.html'

    def get_queryset(self):
        userpk = self.request.user.pk
        queryset = User.objects.filter(pk=userpk)
        return queryset

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    login_url = 'accounts:user_login'
    template_name = 'accounts/account_form.html'

    def get_queryset(self):
        userpk = self.request.user.pk
        queryset = User.objects.filter(pk=userpk)
        return queryset

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('accounts:user_login')
    login_url = 'accounts:user_login'
    template_name = 'accounts/account_confirm_delete.html'
