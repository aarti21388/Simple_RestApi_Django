


# Get one book from DB
## http://127.0.0.1:8000/books_data/GetBook/4

# Get All books
## http://127.0.0.1:8000/books_data/GetBooks/

# With postman apply the following
''''
1. Method = GET 
'''
# Update one Book with id
## http://127.0.0.1:8000/books_data/UpdateBook/2
```
# With postman apply the following
1. Method = PUT 
2. Content = Body>Raw
3. type = JSON

content
--------
    {
        "id": 1,
        "description": "This book is calledharry potterand it is 300 long",
        "title": "harry potter",
        "number_of_pages": 300,
        "publish_date": "2011-02-02",
        "quantity": 30
    },```
```
# Insert new Book data
## http://127.0.0.1:8000/books_data/CreateBook/
'''
# With postman apply the following
1. Method = POST 
2. Content = Body>Raw
3. type = JSON

content
--------
{  
        "description": "This book is called bad bloodand it is 100 long",
        "title": "bad blood",
        "number_of_pages": 100,
        "publish_date": "2022-11-27",
        "quantity": 300
    },'''
```
# Delete one Book with id
## http://127.0.0.1:8000/books_data/DeleteBook/2
'''
# With postman apply the following
1. Method = DELETE 
No Content To Pass
```

