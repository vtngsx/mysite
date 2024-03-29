# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if q:
			if len(q) > 20:
				errors.append('Please enter at most 20 characters.')
			else:
				books = Book.objects.filter(title__icontains=q)
				return render_to_response('search_results.html', {'books': books, 'query': q})
		else:
			errors.append('Enter a search term.')
	return render_to_response('search_form.html', {'errors': errors})
