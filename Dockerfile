#FROM python:3.8

#RUN mkdir /app/

#WORKDIR /app/

#COPY . .

#RUN pip install -r requirements.txt

#FROM baza

#RUN apt update

#RUN apt install --assume-yes gnome-terminal

#CMD ["python", "delete_me.py"]

FROM 66001a317bb6

CMD ["python", "main.py"]