FROM python:3-slim
MAINTAINER jeremialcala@gmail.com

ENV PORT=9830
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update -y
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./

CMD ["python", "main.py"]
EXPOSE 9830
