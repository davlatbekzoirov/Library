from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True).data
        data = {
            'status': f'Returned {len(books)} books',
            'books': serializer
        }

        return Response(data)

# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer



class BookDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book).data

            data = {
                'status': f'Successfull',
                'books': serializer
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': 'Book not found',
                'message': 'Book not found'
            }, status=status.HTTP_404_NOT_FOUND)


# class BookDeleteAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get_object_or_404(pk=pk)
            sertializer = BookSerializer(book).data
            book.delete()
            return Response({
                'status': True,
                'message': 'Book deleted'
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': False,
                'message': 'Book not found'
            }, status=status.HTTP_400_BAD_REQUEST)


# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({
            'status': True,
            'message': 'Book updated'
        }, status=status.HTTP_200_OK)


    def patch(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Book updated'
                }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': False,
                'message': 'Book not found'
            }, status=status.HTTP_400_BAD_REQUEST)


# class BookCreateAPIView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f'Book created successfully',
                'books': data
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)