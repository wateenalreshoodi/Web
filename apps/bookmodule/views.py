from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    # Using render to pass a name variable to the index.html template
    name = request.GET.get("name") or "world!" 
    return render(request, "bookmodule/index.html", {"name": name})  

def index2(request, val1=0):  # Add the view function (index2)
    # Use HttpResponse to return the string directly
    return HttpResponse("value1 = " + str(val1))  

def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)