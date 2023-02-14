FROM python:3.10
LABEL maintainer="Arliadinda Danusaputro"

COPY ./techtrends /techtrends2
WORKDIR /techtrends2
RUN python3 -m pip install -r /techtrends2/requirements.txt

# command to run on container start
CMD [ "python3","/techtrends2/app.py" ]
