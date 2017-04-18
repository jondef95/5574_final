FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3-dev python3-pip git nano
RUN git clone https://github.com/jondef95/5574_final
WORKDIR 5574_final
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python -m nltk.downloader punkt
ENTRYPOINT ["python3"]
CMD ["api_testing.py", "-v"]
