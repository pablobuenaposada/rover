FROM python:3.6.9

WORKDIR /usr/src/app

COPY src /usr/src/app/src
COPY Makefile requirements.txt reviews.csv /usr/src/app

RUN make venv

CMD ["make", "run"]