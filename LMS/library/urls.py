from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_categories, name='list_categories'),
    path('category/<int:id>/', views.books_in_category, name='books_in_category'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('issue_book/', views.issue_book, name='issue_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('users/', views.list_users, name='list_users'),
]