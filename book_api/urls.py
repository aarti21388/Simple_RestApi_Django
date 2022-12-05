from django.urls import path
from . import views

urlpatterns=[
    path("GetBooks/",views.GetBooks.as_view()),
    path("CreateBook/",views.CreateBook.as_view()),
    path("GetBook/<int:pk>",views.GetBook.as_view()),
    path("UpdateBook/<int:pk>",views.UpdateBook.as_view()),
    path("DeleteBook/<int:pk>",views.DeleteBook.as_view()),

    #path("",views.book_create),
    #path("<int:pk>/",views.book),
   # path("book_list")
]

#http://127.0.0.1:9000/books/list/?

#Get one book from DB
#http://127.0.0.1:8000/books_data/GetBook/4

#Get All books
#http://127.0.0.1:8000/books_data/GetBooks/

#Insert new Book data
#http://127.0.0.1:8000/books_data/CreateBook/