#FROM python:3.8

#RUN mkdir /app/

#WORKDIR /app/

#COPY . .

#RUN pip install -r requirements.txt

#RUN apt-get update

#RUN apt-get install ffmpeg libsm6 libxext6  -y

FROM baza

CMD ['python', 'main.py', 'docker']