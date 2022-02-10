from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'python_kubernetes_workflow',
    tags=['baptiste'],
    default_args=default_args,
    schedule_interval=timedelta(minutes=10),
    ) as dag:

    t1 = KubernetesPodOperator(namespace='default',
                          image="Python:3.7",
                          image_pull_policy= 'Never',
                          cmds=["Python","-c","print('hello tast 1 .....................;;')"],
                          labels={"foo": "bar"},
                          name="task-1",
                          is_delete_operator_pod=True,
                          in_cluster=False,
                          task_id="task-1",
                          get_logs=True,
                          )

    t2 = KubernetesPodOperator(namespace='default',
                          image="Python:3.7",
                          image_pull_policy= 'Never',
                          cmds=["Python","-c","print('hello tast 2 .....................;;')"],
                          labels={"foo": "bar"},
                          name="task-2",
                          is_delete_operator_pod=True,
                          in_cluster=False,
                          task_id="task-2",
                          get_logs=True,
                          )

    t1 >> t2
