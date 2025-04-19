FROM python:3.13-slim

WORKDIR /concert_chatapp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

EXPOSE 8000
EXPOSE 8501

CMD ["bash", "run.sh"]
