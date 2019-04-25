FROM python:3.7

RUN mkdir app

WORKDIR app

COPY . ./

CMD [ "python", "app.py" ]
