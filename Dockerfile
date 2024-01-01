FROM python:3.8

WORKDIR /app

COPY . /app

RUN apt-get update -y && pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]