from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Book

# Эндпоинт для списка всех книг
def book_list(request):
    books = list(Book.objects.values())  # Получаем все книги в виде списка словарей
    return JsonResponse(books, safe=False)

# Эндпоинт для получения информации об одной книге
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)  # Получаем книгу по ID или выдаем 404 ошибку
    return JsonResponse({
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "publication_year": book.publication_year
    })
