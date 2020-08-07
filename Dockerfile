FROM selenium/standalone-chrome

WORKDIR /usr/src/app

COPY test_general.py ./

RUN sudo apt update && sudo apt-get install python3.6 && sudo apt install -y python-pip 
RUN pip install keyboard
RUN pip install selenium
RUN pip install pytest

COPY . .

CMD [ "pytest", "./test_general.py"]
