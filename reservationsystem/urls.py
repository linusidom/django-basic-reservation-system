"""reservationsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from reservationsystem import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls'), name='accounts'),
    url(r'^loggedin', views.LoggedInTemplateView.as_view(), name='loggedin'),
 	url(r'^loggedout', views.LoggedOutTemplateView.as_view(), name='loggedout'),
    url(r'^$', views.IndexTemplateView.as_view(), name='index'),
    url(r'^appt/', include('appointments.urls', namespace='appointments')),


    url(r'^change_password/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^change_password_done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name = 'user_login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name = 'user_logout'),

]
