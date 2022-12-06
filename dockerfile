# Build a "BaseImage" 
FROM python:3.9.13

# set environment variables

# it will not check python version

ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# write everything as byte code

ENV PYTHONDONTWRITEBYTECODE 1

# if will pick up from minor changes

ENV PYTHONUNBUFFERED 1

# set work directory (OPT is UNIX optional Folder where we download and run allextenal or 3rd party applications, similar to program files on windows)

RUN mkdir -p /opt/services/books/src

# it is setting as working directory
WORKDIR /opt/services/books/src

# copy the python Library Names and versions of required for our application
#
COPY ./requirements.txt .

#install the specified libraries , it will not create extra cache
#
RUN pip install --no-cache-dir -r requirements.txt

# The project code is copied from the folder where this Dockerfile is located
#
COPY . /opt/services/books/src

# This command Binds Django Application to Gunicon Web server
#

CMD ["python","manage.py","makemigrations"]
CMD ["python","manage.py","migrate"]
CMD ["gunicorn", "--bind" , ":8001", "--workers", "1" , "books.wsgi:application"]

EXPOSE 8001

