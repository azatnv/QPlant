FROM python:3.10.7-slim-bullseye

WORKDIR /usr/src/streamlit
COPY . /usr/src/streamlit/

# RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/src/streamlit/entrypoint.sh"]