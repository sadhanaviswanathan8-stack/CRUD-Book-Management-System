from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(request):                      # READ
    books = Book.objects.all()
    return render(request, 'bookapp/book_list.html', {'books': books})

def book_create(request):                    # CREATE
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookapp/book_form.html', {'form': form})

def book_update(request, pk):                # UPDATE
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookapp/book_form.html', {'form': form})

def book_delete(request, pk):                # DELETE
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookapp/book_confirm_delete.html', {'book': book})