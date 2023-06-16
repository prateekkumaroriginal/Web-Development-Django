from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    all_books = Book.objects.all()
    all_books = Book.objects.all().order_by("title") # gets sorted by title
    all_books = Book.objects.all().order_by("-title") # gets sorted by title in decreasing order
    nr_total_books = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "all_books": all_books,
        "nr_total_books": nr_total_books,
        "avg_rating": avg_rating
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
    })
