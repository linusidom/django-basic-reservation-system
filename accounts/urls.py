from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    # Accounts
    url(r'^signup/$', views.SignUpCreateView.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='user_login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='user_logout'),
    url(r'^update/(?P<pk>\d+)/$', views.AccountUpdateView.as_view(), name='account_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.AccountDeleteView.as_view(), name='account_delete'),
    url(r'^detail/(?P<pk>\d+)/$', views.AccountDetailView.as_view(), name='account_detail'),

]
