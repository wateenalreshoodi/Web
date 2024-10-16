from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))
def viewbook(request, bookId):
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = book1 if book1['id'] == bookId else book2 if book2['id'] == bookId else None
    return render(request, 'bookmodule/show.html', {'book': targetBook})


