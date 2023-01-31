FROM python:3.7-alpine

COPY . /code
WORKDIR /code

RUN pip install --ignore-installed --trusted-host pypi.python.org -r requirements.txt
RUN chmod 644 app.py

EXPOSE 5000

CMD ["python", "app.py"]
