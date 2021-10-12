FROM python:3.9
LABEL maintainer="Dinesh Babu TG <tgdinesh_babu@yahoo.co.in>"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
EXPOSE 8002
ENTRYPOINT [ "python" ]

CMD [ "job_service_app.py" ]