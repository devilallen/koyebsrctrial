FROM python:3.9
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
RUN apt -qq update && apt -qq install -y git python3 python3-pip
COPY . .
RUN pip3 install -r requirements.txt
CMD gunicorn app:app & python main.py
