
import dataset

class Database(object):

	def __init__(self):
		self.db = dataset.connect('sqlite:///:memory:')

	def insert_record(self, table, date, value):
		table = self.db[table]
		table.insert(dict(date=date, value=value))

	def get_records(self, table, date):
		table = self.db[table]
		result = table.find_one(date=date)
