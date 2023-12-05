# Dockerfile.python
FROM python:3.10

WORKDIR /var/www/selenium

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3"]

COPY . .