FROM python:3.10.12


WORKDIR /app


COPY requirements.txt .


RUN python -m pip install -r requirements.txt


COPY . /app


CMD flask --app mainModule/views run -h 0.0.0.0 -p 5000
