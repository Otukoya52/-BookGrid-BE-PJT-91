from django.contrib.auth.models import User
from django.db.models import query
from rest_framework import generics,viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Book, BookReview, Order, OrderItem, Wishlist,WishlistItem
from .serializers import RegisterSerializer,UserSerializer, BookSerializer, BookReviewSerializer,WishlistSerializer, WishlistItemSerializer, OrderSerializer, OrderItemSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterSerializer
    authentication_classes = [JWTAuthentication]

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]


# views for the book model
class BookList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

# views for the book review model
class BookReviewView(viewsets.ModelViewSet):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
#Views for the Cart, Checkout model
class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class WishlistItemView(viewsets.ModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer 
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]   



