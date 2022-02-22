FROM python:3.8

COPY . /CICD

WORKDIR /CICD

RUN pip install --no-cache-dir -r requirements.txt

RUN ["pytest", "-v", "--junitxml=reports/result.xml"]CMD tail -f /dev/null

CMD ["python", "./app.py"]
