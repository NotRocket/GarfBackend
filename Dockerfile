FROM python:3.9

WORKDIR /usr/src/app
COPY ["garf_consumer.py","client.properties", "garf_app.py", "garf_services.py", "garf_sql.py","static","templates", "requirements.txt", "./"]

COPY requirements.txt /usr/src/app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

EXPOSE 5000
#CMD gunicorn -b 127.0.0.1:5000 app:app --timeout 600
CMD ["python", "garf_app.py"]