from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Book, BookReview, Order, OrderItem, Wishlist,WishlistItem,Users

# Serializers for Authentication
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name', 'profile_pic ')

                
# Serializers for the book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'booktype', 'price','e_copy')

    # To show author name instead of id
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['author'] =instance.author.user.username
        return ret

# Serializers for the cart and checkout model

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('id', 'customer','complete')

    # To show author name instead of id
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['author'] =instance.customer.user.username
        return ret

class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = ('book', 'order', 'quantity')
        
# Serializers for the book review model
class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields =('book', 'user', 'comment', 'rating')

#Serializers for wishlist
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('customer', 'complete')

class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('book', 'date')
        model = WishlistItem
        fields = ('book', 'wishlist', 'quantity')        

