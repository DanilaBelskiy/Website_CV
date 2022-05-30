FROM python:3.8

RUN mkdir /app/

WORKDIR /app/

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6  -y

#FROM baza

RUN apt-get install gstreamer1.0-tools -y

#FROM baza_gs

RUN apt-get install -y gstreamer1.0-plugins-good -y

#FROM baza_gs_1

RUN apt-get install -y gstreamer1.0-plugins-ugly

#FROM baza_gs_2

RUN apt install -y gstreamer1.0-plugins-bad

#FROM baza_gs_3

CMD ["python", "main.py", "docker"]