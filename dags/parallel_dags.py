from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='our_first_dag_v6',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2025, 4, 25),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hey, this is the second task!"
    )
    
    task2 >> task1