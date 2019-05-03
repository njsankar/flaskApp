FROM alpine:3.5
RUN apk add --update python py-pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app/hello_world.py /src
COPY app /src/app
CMD python /src/app/hello_world.py