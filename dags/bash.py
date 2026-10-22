from datetime import datetime

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator

# A Dag represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *"):
    # Tasks can be defined by instantiating operators
    hello = BashOperator(task_id="hello", bash_command="echo hello_FRANCISCO")

    # Tasks can be also defined with decorators (Airflow Taskflow syntax)
    @task.bash
    def airflow():
        return "echo airflow_FRANCISCO"

    @task
    def world():
        print("world FRANCISCO")

    # Set dependencies between tasks
    hello >> airflow() >> world()