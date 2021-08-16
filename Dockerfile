FROM python:3.7-slim-buster
WORKDIR /home/app
COPY requirements.txt requirements.txt
RUN apt update && apt install -y build-essential python3-dev python3-tk
RUN pip install -r requirements.txt
COPY . .
CMD python main.py --game-mode manual