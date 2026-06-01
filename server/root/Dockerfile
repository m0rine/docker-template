FROM python:3.12-slim
LABEL authors="Daniel Morine"
# Non buffered python output
ENV PYTHONBUFFERED=1

WORKDIR /server

COPY . .

EXPOSE 8000

CMD ["python3", "-m", "http.server", "8000", "--directory", "."]


