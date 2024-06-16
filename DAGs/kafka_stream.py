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


def get_data():
    """ Gets synthetic data from randomuser.me api. 
        param: :
        returns: 
    """
    # Make a request for data, from 'randomuser' api
    request = requests.get("https://randomuser.me/api/")
    results = request.json()["results"][0]
    # Prints prettier with indentation
    # print(json.dumps(results, indent=3))
    return results


def format_data(result):
    """ Formats the input response data for Kafka 
        :param result: Json response data
        returns: Formatted data
    """
    # Initializing a Dictionary object
    data = {}
    data["first_name"] = result["name"]["first"]
    data["last_name"] = result["name"]["last"]
    


def stream_data():
    """ Streams the data, DAG runs it. 
        :param:
        :returns:
    """
    pass



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
