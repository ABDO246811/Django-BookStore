from django.shortcuts import render


# Create your views here.
def book_detail(request):
    context = {}
    return render(request, 'book_detail.html', context)
