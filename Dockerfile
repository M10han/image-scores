FROM python:3.7.2-slim

#Make a directory for the application
WORKDIR /usr/src/app

#Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copy source code
COPY . /usr/src/app
#COPY start.sh .
RUN chmod a+x start.sh

#Run application
CMD ["./start.sh"]



