FROM selenium/standalone-chrome
LABEL maintainer="jose.castrejon@softtek.com"

EXPOSE 4444

WORKDIR /home/seluser

COPY test_general.py .

RUN sudo chmod +x test_general.py

RUN sudo apt-get update && sudo apt-get install -y python3.6 && sudo apt-get -y install cron && sudo apt install -y python3-pip

RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python


RUN sudo pip3 install keyboard && sudo pip3 install selenium && sudo pip3 install pytest
RUN python3 -m pytest --version


