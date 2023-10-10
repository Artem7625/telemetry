FROM python:3.10-alpine

RUN apk update && \
    apk add py3-pip && \
    apk add alpine-sdk

WORKDIR /src

COPY src /src
COPY requirements.txt /src

RUN pip install -r requirements.txt

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8082"]
CMD ["python3", "main.py"]
