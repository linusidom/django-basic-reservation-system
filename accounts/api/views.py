from rest_framework import generics
from accounts.api.models import AccountsSerializer
from accounts.models import Accounts

class AccountsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	lookup ='pk'
	serializer_class = AccountsSerializer
	queryset = Accounts.objects.all()