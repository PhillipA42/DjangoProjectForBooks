from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    return render(request, "firstApp/home.html")

def createBook(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("read-books")
    context = {"form":form}
    return render(request, "firstApp/form.html", context)

def readBooks(request):
    books = Book.objects.all() # fetches all the book data
    context = {"books":books} 
    return render(request, "firstApp/books.html",context)
   
def readOneBook(request, pk):
    book = Book.objects.get(id=pk)
    context = {"book":book}
    return render(request, "firstApp/book.html",context)

def updateBook(request, pk):
    book = Book.objects.get(id = pk) # fetch the data
    form = BookForm(instance = book) # get the inital book details

    if request.method == "POST":
        form = BookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect("read-books")

    context = {"form":form}
    return render(request, "firstApp/form.html", context)


def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect("read-books")
    context = {"book":book}
    return render(request,"firstApp/delete.html", context)


