from django.contrib import admin
from .models import Users, Book, Order, OrderItem, BookReview, Wishlist, WishlistItem

# Register your models here.
admin.site.register(Users)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(BookReview)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)