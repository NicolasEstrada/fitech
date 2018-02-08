
import json

import arrow
import requests

from common.database import Database


class Fred(Database):

	def __init__(self, observation_start, observation_end,
    	 real_time_start, real_time_end,
    	 api_key, series):

		self._url_template = "{url}/{endpoint}?api_key={api_key}"
		self._observation_start = observation_start
		self._observation_end = observation_end
		self._real_time_start = real_time_start
		self._real_time_end = real_time_end
		self.api_key = api_key
		self.series = series
		Database.__init__(self)

	@staticmethod
	def date_to_year(date):
		return arrow.get(date).year

	def insert_series(self, serie, base_url, endpoint, file_type='json'):

		response = requests.get(
			self._url_template.format(
				url=base_url,
				endpoint=endpoint,
				api_key=self.api_key),
			params = {
				"api_key": self.api_key,
				"observation_start": self._observation_start,
				"observation_end": self._observation_end,
				"real_time_start": self._real_time_start,
				"real_time_end": self._real_time_end,
				"series_id": serie,
				"file_type": file_type
			}
		)

		if response.status_code == 200:
			data = json.loads(response.content)

			for entry in data['observations']:
				try:
					val = float(entry['value'])
				except ValueError:
					# handling FRED's API error, value as '.'
					val = 0.0

				self.insert_record(
					serie,
					arrow.get(entry['date']).datetime.date(),
					val)

		else:
			print(response.content)
			print("Request failed")

	def get_avg_unemployment_by_year(self, serie, start, end):

		results = {}
		for entry in self.db[serie]:
			year = self.date_to_year(entry['date'])
			if year < start or year > end:
				continue
			if year not in results:
				results[year] = []
			results[year].append(entry['value'])

		return {
			year: round(float(sum(values)) / len(values), 2)
			for year, values in results.items()
		}
