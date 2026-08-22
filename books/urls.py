from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListAPIView.as_view(), name='index'),
]