FROM apache/airflow:2.1.1-python3.12
USER root

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

COPY dags /opt/airflow/dags
COPY scripts /opt/airflow/dags/scripts
COPY data /opt/airflow/data

USER airflow
