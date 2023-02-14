FROM python:3.10
LABEL maintainer="Arliadinda Danusaputro"

COPY . /techtrends
WORKDIR /techtrends
RUN python3 -m pip install -r requirements.txt

# command to run on container start
CMD [ "python3","app.py" ]
