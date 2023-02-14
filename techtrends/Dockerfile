FROM python:3.10
LABEL maintainer="Arliadinda Danusaputro"

COPY ./techtrends /techtrends
WORKDIR /techtrends
RUN python3 -m pip install -r ./techtrends/requirements.txt

# command to run on container start
CMD [ "python3","./techtrends/app.py" ]
