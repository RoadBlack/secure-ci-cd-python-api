FROM ubuntu:22.04
# Set working directory.
COPY /app /app
COPY ./requirements.txt /app
WORKDIR /app
# For troubleshooting
#RUN ls /app && sleep 40
#RUN pwd && ls -la && cat requirements.txt

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt
EXPOSE 8000

CMD [ "fastapi",  "run", "main.py", "--host", "0.0.0.0", "--port", "8000" ]
