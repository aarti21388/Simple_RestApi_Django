from django.shortcuts import render

from .book import Book

from django.http import HttpResponse,JsonResponse

from .bookserializer import BookSerializer

from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView

from rest_framework.decorators import api_view

# Create your views here.

#Get all Books
class GetBooks(ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
   
#Create Book
class CreateBook(CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

#Get one book accoring to pk
class GetBook(RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class UpdateBook(UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
class DeleteBook(DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    

# @api_view(['GET'])
# def books_list(request):
#     books=Book.objects.all() #complex data
#     serilizer=BookSerializer(books,many=True)
#     #bookPython=list(books.values()) #python datastructor
#     return Response(serilizer.data)


# @api_view(['POST'])
# def book_create(request):
#     serilizer=BookSerializer(data=request.data)
#     if serilizer.is_valid():
#         serilizer.save()
#         return Response(serilizer.data)
#     else:
#         return Response(serilizer.errors)

# @api_view(['GET','PUT','DELETE'])
# def book(request,pk):
#     book=Book.objects.get(pk=pk)
#     if request.method=='GET':

#         seralizer=BookSerializer(book)
#         return Response(seralizer.data)
    
#     if request.method=='PUT':
#         seralizer=BookSerializer(book,data=request.data)
#         if seralizer.is_valid():
#             seralizer.save()
#             return Response(seralizer.data)
#         return Response(seralizer.errors)

    