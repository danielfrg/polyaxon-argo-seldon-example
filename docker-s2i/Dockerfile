FROM docker:18.06.1-ce

ADD https://github.com/openshift/source-to-image/releases/download/v1.1.10/source-to-image-v1.1.10-27f0729d-linux-amd64.tar.gz s2i.tar.gz
RUN tar -xvf s2i.tar.gz
RUN mv s2i /usr/local/bin

RUN mkdir -p /src
WORKDIR /src
