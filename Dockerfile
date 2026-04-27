FROM python:3.12-slim

WORKDIR /the-internet-tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \ 
    python -m playwright install --with-deps

COPY . .

ENTRYPOINT [ "pytest" ]