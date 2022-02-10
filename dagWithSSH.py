from datetime import timedelta, datetime
import airflow
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime.now() - timedelta(minutes=20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(dag_id='example_with_ssh',
          tags=['baptiste'],
          default_args=default_args,
          schedule_interval='0,10,20,30,40,50 * * * *',
          dagrun_timeout=timedelta(seconds=120))
# Step 1 - Execute bash on remote server
t1_bash = """
echo 'Hello World'
pwd
ls
echo $USER
/tmp/runTest.sh
"""
#SSH_LOCAL is a SSH connection defined in airflow UI, Admin->connection-> (connection type : SSH, Host : 172.20.0.1, user : airflowssh , password : ******)
t1 = SSHOperator(
    ssh_conn_id='SSH_LOCAL',
    task_id='test_ssh_operator',
    command=t1_bash,
    dag=dag)
