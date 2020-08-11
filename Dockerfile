FROM selenium/standalone-chrome
LABEL maintainer="jose.castrejon@softtek.com"

EXPOSE 4444

WORKDIR /home/seluser

COPY test_general.py .
COPY entrypoint.sh .

RUN sudo chmod +x entrypoint.sh && sudo chmod +x test_general.py

RUN sudo apt-get update && sudo apt-get install -y python3.6 && sudo apt-get -y install cron

RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python

RUN sudo pip install keyboard && sudo pip install selenium && sudo pip install pytest
RUN pytest --version
#Adding cron job
ENTRYPOINT ["/bin/bash", "-c","/home/seluser/entrypoint.sh"]
