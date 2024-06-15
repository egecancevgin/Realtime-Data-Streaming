import json
import datetime
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator


# Indicates default configurations for DAG
# !datetime() method should be called from datetime.datetime!
default_args = {
    'owner': 'vboxuser',
    'start_date': datetime.datetime(2023, 9, 3, 10, 00)
}


def stream_data():
    """ Streams data, DAG runs it. 
        param: :
        returns: 
    """
    # Make a request for data, from 'randomuser' api
    request = requests.get("https://randomuser.me/api/")
    results = request.json()["results"][0]
    # Prints prettier with indentation
    print(json.dumps(results, indent=3))


stream_data()

"""
with DAG(
    "user_automation",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False) as dag:
    streaming_task = PythonOperator(
        task_id="stream_data_from_api",
        python_callabe=stream_data)
"""
