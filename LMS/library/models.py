from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    published_date = models.DateField()
    copies_available = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__ (self):
        return self.name

class User(models.Model):
    username =models.CharField(max_length=100,unique=True)
    email =models.EmailField()
    pho_num =models.CharField(max_length=10,blank=True,null=True)   

    def __str__(self):
        return self.username

class Issue_book(models.Model):
    book =models.ForeignKey('Book',on_delete=models.CASCADE)
    user =models.ForeignKey('User',on_delete=models.CASCADE)
    issue_date =models.DateField()
    return_date =models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.book.title