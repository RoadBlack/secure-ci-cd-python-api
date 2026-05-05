FROM ubuntu:24.04
# Set working directory.
COPY /app /app
COPY ./requirements.txt /app
WORKDIR /app
# For troubleshooting
#RUN ls /app && sleep 40
#RUN pwd && ls -la && cat requirements.txt
#Installing globbaly python3 and pip3
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv
#Seperating enviroment because of pip668 
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r requirements.txt
EXPOSE 8000

CMD [ "fastapi",  "run", "main.py", "--host", "0.0.0.0", "--port", "8000" ]
