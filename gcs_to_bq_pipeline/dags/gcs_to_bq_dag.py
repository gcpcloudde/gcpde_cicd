from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

# Default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 1),
    'retries': 1,
}

# DAG Definition
with DAG('gcs_to_bq_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    # Task 1: Load data from GCS to BigQuery
    load_gcs_to_bq = GCSToBigQueryOperator(
        task_id='load_gcs_to_bq',
        bucket='gcp-pandas-buc1',
        source_objects=['ticket_data_march_2025_03_03.csv'],
        destination_project_dataset_table='long-perception-447114-s0.newbatch.ticket_data',
        write_disposition='WRITE_APPEND',
        source_format='CSV',
        autodetect=True,
    )

    load_gcs_to_bq 
