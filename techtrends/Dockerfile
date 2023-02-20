FROM python:3.10
LABEL maintainer="Arliadinda Danusaputro"

COPY ./ ./techtrends
WORKDIR ./techtrends
# install requirements 
RUN python3 -m pip install -r requirements.txt

# pre define init db
CMD [ "python3","init_db.py" ]

# expose port 3111
EXPOSE 3111

# command to run on container start
CMD [ "python3","app.py" ]
