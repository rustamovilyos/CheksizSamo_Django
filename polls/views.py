from django.shortcuts import render
from django.views.generic import ListView, DetailView
from polls.models import Janrlar, Kitoblar


def index(request):
    janrlar = Janrlar.objects.all()
    kitoblar = Kitoblar.objects.all()
    return render(request, 'polls/index.html', {'janrlar': janrlar, 'kitoblar': kitoblar})


def kitob(request, kitob_id):
    books_list = Kitoblar.objects.all()
    janrlar = Janrlar.objects.all()
    kitob_janr = Janrlar.objects.get(pk=kitob_id)
    count_book = Kitoblar.objects.count()
    all_books = Kitoblar.objects.filter(janri=kitob_janr)
    return render(request, 'polls/index.html',
                  {'janrlar': janrlar, 'all_books': all_books, 'books_list': books_list, 'count_book': count_book})
