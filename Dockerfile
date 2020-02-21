FROM alpine:3.11

RUN apk add --no-cache python3-dev \
    && apk add --no-cache build-base \
    && apk add --no-cache libffi-dev \
    && apk add --no-cache openssl-dev \
    && pip3 install --upgrade pip


WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "app.py"]