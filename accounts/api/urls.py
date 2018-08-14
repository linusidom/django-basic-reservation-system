from django.conf.urls import url
from accounts.api import views
app_name = 'api_accounts'
urlpatterns = [
	url(r'(?P<pk>\d+)',views.AccountsRUDAPIView.as_view(),name='api_accounts'),
]
