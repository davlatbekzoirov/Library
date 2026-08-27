from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'books', views.BookViewSet, basename='books')

urlpatterns = [
    # path('books', views.BookListAPIView.as_view()),
    # # path('', views.book_list_view),
    # path('books/<int:pk>', views.BookDetailAPIView.as_view()),
    # path('books/<int:pk>/update', views.BookUpdateAPIView.as_view()),
    # path('books/<int:pk>/delete', views.BookDeleteAPIView.as_view()),
    # path('books/create', views.BookCreateAPIView.as_view()),
    # path('booklistcreate', views.BookListCreateAPIView.as_view()),
    # path('bookupdatedelete/<int:pk>', views.BookUpdateDeleteAPIView.as_view()),
]

urlpatterns += router.urls