FROM python:3.7.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /home/app

WORKDIR /home/app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

EXPOSE 8000

CMD [ "sh", "./entrypoint.sh" ]