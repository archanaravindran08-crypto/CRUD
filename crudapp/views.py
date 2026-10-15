from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# CREATE and READ
def book_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        price = request.POST.get("price")

        if title and author and price:
            Book.objects.create(
                title=title,
                author=author,
                price=int(price)
            )
            return redirect("book_list")

    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


# UPDATE book price
def update_price(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        price = request.POST.get("price")

        if price and price.isdigit():
            book.price = int(price)
            book.save()
            return redirect("book_list")

    return render(request, "update_price.html", {"book": book})


# DELETE book
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "delete_book.html", {"book": book})