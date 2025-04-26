FROM apache/airflow:2.10.5-python3.11
COPY dags/ $AIRFLOW_HOME/dags

    