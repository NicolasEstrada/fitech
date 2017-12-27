# fitech - FRED app

Financial app to get information from Federal Reserve's FRED API.

## Description

This application fetch data from FRED's API and store it in sqlite in-memory database.

Is written in Python 2.7.10 using following libraries:

* [Arrow](https://http://arrow.readthedocs.io/)
* [Dataset](http://docs.python-requests.org/en/stable/)
* [Dataset](https://dataset.readthedocs.io/en/latest/)

All requirements are stored within requirements.txt file with correspondent versions.

## Structure

The main folder of this application is:

```bash
fitech
├── Dockerfile
├── README.md
├── LICENSE
├── __init__.py
├── app.py
├── common
│   ├── __init__.py
│   ├── database.py
│   ├── fred.py
├── config
│   ├── __init__.py
│   ├── parameters.py
└── requirements.txt 
```

The `app.py` is the Python application that handles all parameters and execution details.

Within `config/` folder, there is one file for configuration parameters used as default.

The `common/` folder's purpose is to contain all common classes and execution. For instance, `database.py` contains database handler and `fred.py` contains API request handling.

## Building and deployment

Fred App has its own Dockerfile to be built and deployed using any container manager that is compatible with it.
To create the docker image (be sure to put the API key used or set it as env variable under FRED_API_KEY), just run within `fithech/` the following:

```bash
docker build -t fitech .
```

Another option is to install requirements with pip and run it manually from `fitech/`:

```bash
pip install -r requirements.txt
python app.py --ak "YOUR_API_KEY"

```

## App Help Instructions

```bash
usage: app.py [-h] [-os OBSERVATION_START] [-oe OBSERVATION_END]
              [-rts REAL_TIME_START] [-rte REAL_TIME_END] [-ak API_KEY]
              [-s SERIES [SERIES ...]]

App to fetch and store FRED API data.

optional arguments:
  -h, --help            show this help message and exit
  -os OBSERVATION_START, --observation_start OBSERVATION_START
                        Start point for data fetch. (default: 1776-07-04)
  -oe OBSERVATION_END, --observation_end OBSERVATION_END
                        End point for data fetch. (default: 9999-12-31)
  -rts REAL_TIME_START, --real_time_start REAL_TIME_START
                        Start point for realtime fetch. (default: 1776-07-04)
  -rte REAL_TIME_END, --real_time_end REAL_TIME_END
                        End point for realtime fetch. (default: 9999-12-31)
  -ak API_KEY, --api_key API_KEY
                        API key to be used for FRED requests. (default: None)
  -s SERIES [SERIES ...], --series SERIES [SERIES ...]
                        List of series to use. (default: ['GDPC1', 'UMCSENT',
                        'UNRATE'])
```