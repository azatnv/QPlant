FROM ubuntu:20.04

WORKDIR /usr/src/fastapi
COPY . /usr/src/fastapi/


# Install OpenJDK-8 and Python
RUN apt-get update && \
    apt-get install -y openjdk-8-jre && \
    apt-get install -y ant && \
    apt-get install -y python && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;


# Setup JAVA_HOME -- useful for docker commandline
# ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
# RUN export JAVA_HOME

RUN apt-get update && apt-get install -y python3-pip
# RUN pip3 install -r requirements.txt
RUN pip install -r requirements.txt

# RUN apt-get install dos2unix

ENTRYPOINT ["/usr/src/fastapi/entrypoint.sh"]