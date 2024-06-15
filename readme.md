To start building a virtual environment in Visual Studio Code:
``` bash
apt update
apt upgrade
apt install python3.10-venv
python3 -m venv .venv
```

Project starts with './DAGs/kafka_stream.py', defining the initial default configurations for DAG to use:
``` python
default_args = {
    'owner': 'vboxuser',
    'start_date': datetime(2023, 9, 3, 10, 00)
}
```

Creating a data streaming function which makes requests from the 'randomuser' api:
``` python

```

Creating a DAG instance with the following arguments:

