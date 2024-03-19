# dockerfile for practicing how to use docker
FROM ubuntu.2.14.3

#-y to make the apt install py without intruptions
RUN apt-get update &&
    apt-get install -y python3 &&
    pip install scrapy, pipenv &&
    pipenv install scrapy &&
    scrapy crawl hummusspider.py -o

