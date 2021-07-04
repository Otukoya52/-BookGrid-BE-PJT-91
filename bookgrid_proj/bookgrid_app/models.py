from django.db import models
from django.contrib.auth.models import User

# Write your models here.

class Users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username       

class Book(models.Model):
    book_choices = (('1',"new_product"),('2',"old_product"))
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    e_copy = models.BooleanField(default=True)
    booktype = models.CharField(choices=book_choices,max_length=50,null=True,blank=True)
    price = models.CharField(max_length=100,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title 

# Models for cart and chheckout
class Order(models.Model):
    customer = models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,blank=True)
    complete = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer  

class OrderItem(models.Model):
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)    
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order} - {self.book}'

# model for the book review section
class BookReview(models.Model):
  book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
  customer = models.ForeignKey(Users, related_name='reviews', on_delete=models.CASCADE,null=True)
  comment = models.TextField(blank=True, null=True)
  rating = models.IntegerField(default=0)
  date_added = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    customer = models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,blank=True)
    complete = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer  

class WishlistItem(models.Model):
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True,blank=True)
    wishlist = models.ForeignKey(Wishlist,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)    
    date_ordered = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f'{self.wishlist} - {self.book}'
