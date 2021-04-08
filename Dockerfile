FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# RUN python manage.py makemigrations

# RUN python manage.py migrate

#RUN python manage.py collectstatic

# CMD [ "python", "manage.py", "runserver" , "0.0.0.0:8000"]
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000