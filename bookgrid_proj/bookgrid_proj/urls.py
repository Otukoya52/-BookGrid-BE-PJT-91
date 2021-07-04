"""bookgrid_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from bookgrid_app import views
from bookgrid_app.views import RegisterView,UserView, BookReviewView 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()
router.register('book',views.BookList,basename='BookList')
router.register('bookreview',views.BookReviewView,basename='BookReview')
router.register('order',views.OrderView,basename='Order')
router.register('orderitem',views.OrderItemView,basename='OrderItem')
router.register('wishlist',views.WishlistView,basename='WishlistView')
router.register('wishlistitem',views.WishlistItemView,basename='WishlistItem')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken',TokenObtainPairView.as_view(),name="gettoken"),
    path('api/refresh_token',TokenRefreshView.as_view(),name="refresh_token"),
    path('register/',RegisterView.as_view(),name="register"),
    path('user/',UserView.as_view(),name="user"),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]