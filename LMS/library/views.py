from django.shortcuts import render
from .models import Book,Category,User,Issue_book
# Create your views here.


def list_categories(request):
    categories = Category.objects.all()
    return render (request,'list_categories.html',{'categories':categories})

def books_in_category(request,id):
    category = Category.objects.get(id=id)
    books = Book.objects.filter(category=category)
    return render (request,'books_in_category.html',{'books':books})

def book_detail(request,id):
    book = Book.objects.get(id=id)
    return render (request,'book_detail.html',{'book':book})

def issue_book(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        user_id = request.POST['user_id']
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=user_id)
        issue = Issue_book(book=book,user=user)
        issue.save()
        book.copies_available -= 1
        book.save()
        return redirect('issue_book')
    return render (request,'issue_book.html',{'books':Book.objects.all(),'users':User.objects.all()})

def return_book(request):
    if request.method == 'POST':
        issue_id = request.POST['issue_id']
        issue = Issue_book.objects.get(id=issue_id)
        book = issue.book
        book.copies_available += 1
        book.save()
        issue.delete()
        return redirect('return_book')
    issues = Issue_book.objects.all()
    return render(request, 'return_book.html', {'issues': issues})

def list_users(request):
    users = User.objects.all()
    user_issues = {user: Issue_book.objects.filter(user=user) for user in users}
    return render(request, 'list_users.html', {'user_issues': user_issues})
