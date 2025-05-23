FROM python:3.11

WORKDIR /usr/src/app

COPY sender.py .
COPY requirements.txt .
COPY data/ data/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "sender.py"]