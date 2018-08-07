from django.conf.urls import url
from appointments import views

app_name = 'appointments'

urlpatterns = [
    url(r'^create/$', views.new_appointment,name='appointment_create'),
 	url(r'^list/$', views.AppointmentListView.as_view(),name='appointment_list'),
    url(r'^detail/(?P<pk>\d+)/$', views.AppointmentDetailView.as_view(),name='appointment_detail'),
    url(r'^update/(?P<pk>\d+)/$', views.AppointmentUpdateView.as_view(),name='appointment_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.AppointmentDeleteView.as_view(),name='appointment_delete'),   
]
