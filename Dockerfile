FROM python:3.10-alpine

ARG FITBUZZ_SECRET_KEY
ENV PYTHONUNBUFFERED 1
ENV FITBUZZ_SECRET_KEY ${FITBUZZ_SECRET_KEY}

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY fitbuzz /app/fitbuzz

WORKDIR /app/fitbuzz

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
RUN python manage.py makemigrations app
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]