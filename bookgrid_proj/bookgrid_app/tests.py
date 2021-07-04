from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book

# Create your tests here.

# Tests for the Book model
class BookModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #create a User
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        testuser1.save()

        # Add a book 
        test_book = Book.objects.create(
            author=testuser1, title='how to test in django',
            booktype=2, price=2400044
            )
        test_book.save()

    def test_book_content(self):
        book = Book.objects.get(id=1)
        author = f'{book.author}'
        title = f'{book.title}'
        booktype = f'{book.booktype}'
        price = f'{book.price}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'how to test in django')
        self.assertEqual(booktype, '2')
        self.assertEqual(price, '2400044')