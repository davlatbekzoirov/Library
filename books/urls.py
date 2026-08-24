from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListAPIView.as_view()),
    # path('', views.book_list_view),
    path('<int:pk>', views.BookDetailAPIView.as_view()),
    path('<int:pk>/update', views.BookUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.BookDeleteAPIView.as_view()),
]
