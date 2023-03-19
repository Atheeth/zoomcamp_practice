FROM python:3.9

RUN pip install --upgrade pip

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

COPY ingest_data.py ingest_data.py
COPY output.csv output.csv

ENTRYPOINT ["python","ingest_data.py"]