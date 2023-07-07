FROM python:3.11.4

# create non-root user
RUN groupadd -r docker \
    && useradd -r -g docker -s /bin/bash -m docker

# Install requried packages
# Note: chromium is needed for creating pdf via marp. If you do not use marp
#       you can skip installing chromium.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    git \
    make \
    # chromium \
    && rm -rf /var/lib/apt/lists/*

# Setup working directory
WORKDIR /tmp/work

COPY requirements.txt ${PWD}

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN pylint --generate-rcfile > .pylintrc

ENV PYTHONPATH "${PYTHONPATH}:/tmp/work/src"

# set non root user
USER docker
