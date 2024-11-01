"""
postgres_to_snowflake
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
import pendulum

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from airflow.operators.postgres_operator import PostgresOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG(
    'my_new_dag',
    default_args=default_args,
    schedule_interval='@daily',
)
start = SQLExecuteQueryOperator(
    task_id="create_pet_table",
    conn_id="postgres"
    sql="""
        CREATE TABLE IF NOT EXISTS pet (
        pet_id SERIAL PRIMARY KEY,
        name VARCHAR NOT NULL,
        pet_type VARCHAR NOT NULL,
        birth_date DATE NOT NULL,
        OWNER VARCHAR NOT NULL);
        """,
)
end = DummyOperator(task_id='end', dag=dag)

start >> end


default_args={
    "owner": "Chauncey I. Plummer,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2024-10-27", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "Chauncey I. Plummer": "mailto:chaunceyplum@gmail.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/cm2rwddbw0bp601jtwk6mkhdc/cloud-ide/cm2rworcv0c1701kdq8j2ldnq/cm2rwpnio0bwj01jjnt3js4ka",
    },
)
def postgres_to_snowflake():

dag_obj = postgres_to_snowflake()
