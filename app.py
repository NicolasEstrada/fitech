
import os
import json
import argparse

from common.fred import Fred
from config import parameters

if __name__ == '__main__':

    # FRED API analyzer app

    parser = argparse.ArgumentParser(
        description="App to fetch and store FRED API data.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-os',
        '--observation_start',
        default='1776-07-04',
        help='Start point for data fetch.')

    parser.add_argument(
        '-oe',
        '--observation_end',
        default='9999-12-31',
        help='End point for data fetch.')

    parser.add_argument(
        '-rts',
        '--real_time_start',
        default='1776-07-04',
        help='Start point for realtime fetch.')

    parser.add_argument(
        '-rte',
        '--real_time_end',
        default='9999-12-31',
        help='End point for realtime fetch.')

    parser.add_argument(
        '-ak',
        '--api_key',
        default=os.environ.get('FRED_API_KEY'),
        help='API key to be used for FRED requests.')

    parser.add_argument(
        '-s',
        '--series',
        default=parameters.SERIES,
        nargs = '+',
        help='List of series to use.')

    args = parser.parse_args()

    fred_app = Fred(args.observation_start, args.observation_end,
         args.real_time_start, args.real_time_end,
         args.api_key, args.series)

    for serie in args.series:
        # for each series passed as arguments, insert data
        fred_app.insert_series(
            serie,
            parameters.BASE_URL,
            parameters.SERIES_ENDPOINT
        )

    r = fred_app.get_avg_unemployment_by_year('UNRATE', 1980, 2015)
    print(r)