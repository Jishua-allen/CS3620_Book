from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator

# Create your views here.


def index(request):
  return render(request, 'index.html')

def book_list(request):
  book_list = Book.objects.all()
  book_name = request.GET.get('search')
  print(book_name)
  if book_name is None:
    book_name = ''  
  if book_name != '' and book_name is not None:
    book_list = book_list.filter(title__icontains=book_name)
  paginator = Paginator(book_list, 5)
  page = request.GET.get('page')
  book_list = paginator.get_page(page)
  print(book_name)
  context = {
    'book_list': book_list,
    'search_value': book_name
  }
  return render(request, 'Book/book_list.html', context)
