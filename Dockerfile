FROM selenium/standalone-chrome
LABEL maintainer="jose.castrejon@softtek.com"

EXPOSE 4444

WORKDIR /home/seluser

COPY test_general.py .

RUN sudo apt-get update 
RUN sudo apt-get install -y python3.6

RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python

RUN sudo pip install keyboard
RUN sudo pip install selenium
RUN sudo pip install pytest
RUN pytest --version
