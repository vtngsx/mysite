# Create your views here.

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from contact.forms import ContactForm

def contact(request):
	errors = []
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			#send_mail(
			#	cd['subject'],
			#	cd['message'],
			#	cd.get('e-mail', 'noreply@example.com'),
			#	['siteowner@example.com'],
			#)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		#form = ContactForm(initial={'subject': 'I love your site!'})
		form = ContactForm()
	return render_to_response('contact_form.html', {'form' : form}, context_instance=RequestContext(request))

def thanks(request):
	return render_to_response('contact_thanks.html')