FROM python:3.12 AS builder

WORKDIR /RamblerToTelegram
COPY requirement.txt ./
RUN python -m venv ./venv \
    && source venv/bin/activate \
    && pip install -r --no-cache-dir requirement.txt

FROM python:3.12-slim

WORKDIR /RamblerToTelegram

COPY --from=builder /RamblerToTelegram ./
COPY app.py ./
COPY config.py ./
COPY emailer.py ./
CMD source venv/bin/activate
CMD ["python3", "app.py"]