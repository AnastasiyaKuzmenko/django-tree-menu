FROM python:3.15-slim

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip && pip --no-cache-dir install -r /app/requirements.txt

RUN chmod +x /app/entrypoint.sh
CMD [ "/app/entrypoint.sh" ]
