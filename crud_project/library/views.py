from django.shortcuts import render,redirect
from library.forms import BookForm
from library.models import Book
# Create your views here.
def lib(request):  
    if request.method == "POST":  
        form = BookForm(request.POST, request.FILES)
        print(form.errors)  
        if form.is_valid():  
            try:  
                form.save()
                img_obj = form.instance
                return redirect('/show',{'img_obj': img_obj})  
            except:  
                pass  
    else:  
        form = BookForm()  
    return render(request,'index.html',{'form':form})

def show(request):  
    books = Book.objects.all().order_by('id')  
    return render(request,"show.html",{'books':books})

def edit(request, id):  
    book = Book.objects.get(id=id)
    issue_date = str(book.bissuedate)
    return render(request,'edit.html', {'book':book, 'pub_choice':Book.PUBLISHER_CHOICE, 'issue_date':issue_date, 'issue_choice':BookForm.ISSUE_CHOICES, 'loc_choice':BookForm.LOCATION_CHOICES})

def update(request, id):  
    book = Book.objects.get(id=id)
    form = BookForm(request.POST, request.FILES, instance = book)
    print(form.errors)
    if form.is_valid():
        img_obj = form.instance
        form.save()
        return redirect("/show",{'img_obj': img_obj})  
    return render(request, 'edit.html', {'book': book})

def destroy(request, id):  
    book = Book.objects.get(id=id)  
    book.delete()  
    return redirect("/show") 