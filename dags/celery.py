from airflow.sdk import dag, task
from time import sleep

@dag
def celery_dag():
    
    @task
    def a():
        sleep(5)
        
    @task
    def b(
        queue="high_cpu"
    ):
        sleep(5)

    @task
    def c(
        queue="high_cpu"
    ):
        sleep(5)
        
    @task
    def d(
        queue="high_cpu"
    ):
        sleep(5)
        
    a() >> [b(), c()] >> d()
    

celery_dag()