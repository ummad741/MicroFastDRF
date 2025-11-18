FROM python:3.10.12
ENV PYTHONUNBUFFERED 1
COPY ./entrypoint.sh /
# executable entrypoint.sh with absolute numbers
RUN chmod 777 /entrypoint.sh
WORKDIR /micro
COPY src/requirements.txt /micro/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /micro/