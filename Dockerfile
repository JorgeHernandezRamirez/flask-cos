FROM python:3.9-alpine
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
RUN mkdir ~/.bluemix
EXPOSE 8080
CMD [ "python", "app.py" ]