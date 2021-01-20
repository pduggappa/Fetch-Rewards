FROM python:3.6.1-alpine
COPY . /app
WORKDIR /app
#ADD . /project
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["python3"]
CMD ["app.py"]