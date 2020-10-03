from django.shortcuts import render
from .models import Book

# Create your views here.


def book_detail(request, id):
    book_detail = Book.objects.get(id =id)
    context = {'book' : book_detail}
    return render(request, 'book_detail.html', context)
