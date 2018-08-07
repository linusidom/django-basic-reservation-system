from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
	template_name = 'index.html'

class LoggedInTemplateView(TemplateView):
	template_name = 'loggedin.html'

class LoggedOutTemplateView(TemplateView):
	template_name = 'loggedout.html'