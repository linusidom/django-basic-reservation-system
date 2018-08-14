# from django.urls import path, re_path
from accounts import views
from django.conf.urls import url


app_name='accounts'

urlpatterns=[
	url(r'^$',views.IndexTemplateView.as_view(), name = 'index'),
	url(r'^signup/$',views.signup, name = 'signup'),
	url(r'^detail/(?P<pk>\d+)/$',views.ProfileDetailView.as_view(), name = 'profile_detail'),
	url(r'^update/(?P<pk>\d+)/$',views.update_profile, name = 'profile_update'),
	url(r'^delete/(?P<pk>\d+)/$',views.ProfileDeleteView.as_view(), name = 'profile_delete'),

]