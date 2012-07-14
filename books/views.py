# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book

def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if q:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html', {'books': books, 'query': q})
		else:
			error = True
	return render_to_response('search_form.html', {'error': error})
