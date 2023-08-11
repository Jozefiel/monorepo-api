FROM python:3.10-buster as builder

RUN : \
	&& apt-get -y update \
	&& apt-get -y upgrade \
	&& rm -rf /var/lib/apt/lists/*

RUN pip3 install poetry

WORKDIR /home/app
COPY . .

RUN poetry build

FROM python:3.10-buster

LABEL maintainer="Jozef Volak <jozefvolak@gmail.com>"

COPY --from=build /home/app/dist/*.whl /home/app

RUN pip install "/home/app/*.whl"

ENTRYPOINT ["bash"]