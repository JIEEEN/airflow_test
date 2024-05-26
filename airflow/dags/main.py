from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# DAG 설정
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 24),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1),
)

# 시작 Task
start_task = DummyOperator(task_id='start_task', dag=dag)

# Python 함수 정의
def print_hello():
    return 'Hello Airflow!'

# Python Operator
python_task = PythonOperator(
    task_id='python_task',
    python_callable=print_hello,
    dag=dag,
)

# 끝 Task
end_task = DummyOperator(task_id='end_task', dag=dag)

# Task 간의 관계 정의
start_task >> python_task >> end_task
