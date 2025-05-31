FROM python:3.10-alpine

# Curl for health checks
RUN apk add --no-cache curl

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "fastapi", "run", "--reload" ]

