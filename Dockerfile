FROM selenium/standalone-chrome

WORKDIR /usr/src/app

COPY test_general.py ./

RUN apt update && apt install -y pip
RUN pip install keyboard
RUN pip install selenium
RUN pip install pytest

COPY . .

CMD [ "pytest", "./test_general.py"]
