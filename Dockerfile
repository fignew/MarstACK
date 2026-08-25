FROM python:3.12-alpine

ENV LOG_LEVEL=info

WORKDIR /code/app
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

# Install system-wide as root BEFORE switching users. A user-site
# (~/.local) install would depend on $HOME at runtime and break when the
# container/add-on runs as a different user than the one that installed.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN adduser --disabled-password --gecos "MarstACK" mack \
 && chown -R mack:mack /code

USER mack

CMD ["/bin/sh", "-c", "uvicorn main:app --log-level ${LOG_LEVEL} --host 0.0.0.0 --port 8000"]
