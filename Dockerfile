FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN pip install gunicorn

RUN mkdir -p /hs/async
WORKDIR /hs/async

COPY requirements.txt /hs/async
RUN pip install --no-cache-dir -r requirements.txt

COPY async/. /hs/async

CMD ["./start.sh"]
