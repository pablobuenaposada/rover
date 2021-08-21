FROM python:3.6.9

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN make venv

CMD ["make", "run"]