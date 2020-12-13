FROM python:3.9-slim-buster

RUN apt update && \
    apt install -y \
    libspatialindex-dev \
    libgeos-dev \
    fontconfig \
    unzip

ARG WORKDIR
WORKDIR $WORKDIR
COPY . .

RUN mkdir /usr/share/fonts/truetype/jost/
RUN unzip -d /tmp font/Jost.zip
RUN mv /tmp/TrueType/*.ttf /usr/local/share/fonts/
RUN fc-cache -fv

RUN mkdir -p venvs
RUN python3 -m venv venvs/2020_map
RUN venvs/2020_map/bin/pip install --upgrade pip
RUN venvs/2020_map/bin/pip install -r requirements.txt
ENV MPLCONFIGDIR "/tmp"

ARG BUILD_DATE
ARG NAME
ARG ORG
ARG VCS_REF
ARG VENDOR
ARG VERSION

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name=$NAME \
      org.label-schema.description="Builds a 2020 electoral map" \
      org.label-schema.url="https://github.com/${ORG}/${NAME}" \
      org.label-schema.vcs-url="https://github.com/${ORG}/${NAME}" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vendor=$VENDOR \
      org.label-schema.version=$VERSION \
      org.label-schema.docker.schema-version="1.0" \
      org.label-schema.docker.cmd="docker run {ORG}/${NAME}"

CMD ["venvs/2020_map/bin/python3", "build_map.py"]