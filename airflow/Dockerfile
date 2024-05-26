FROM python:3.8-slim-buster
LABEL maintainer="jieeen"

USER root

RUN apt-get update && apt-get install -y \
  build-essential \
  default-libmysqlclient-dev \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2-binary
RUN pip install apache-airflow

ENV AIRFLOW_HOME=/usr/local/airflow

RUN useradd -ms /bin/bash airflow

RUN mkdir -p /usr/local/airflow/logs /usr/local/airflow/dags /usr/local/airflow/plugins \
  && chown -R airflow:airflow /usr/local/airflow

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# USER airflow

ENTRYPOINT ["/entrypoint.sh"]
