FROM python:latest

WORKDIR /flask

COPY flask /flask
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "app:create_app()" ]