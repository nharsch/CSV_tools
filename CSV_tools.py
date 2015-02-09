# util script to create useful object to hold CSV values for reading and writing

import csv

class CsvTable:
	'''
	creates data structure to hold info about a csv file
	uses first row as header values
	stores rows as dicts within a list (.dicter)
	can write out to new csv file with .write_out(output tag)
	'''
	def __init__(self, csv_name):
		'''takes a csv and initializes object'''
		self.csv_name = csv_name #this is the filename
		self.csv_file = open(csv_name, 'rU') #open file in Universal read line
		self.csv_headers = csv.reader(self.csv_file).next()
		self.dicter = [row for row in csv.DictReader(self.csv_file, fieldnames=self.csv_headers)] #list of dicts


	def write_out(self, output_tag):
		'''write csv file with appended output tag'''
		with open(self.csv_name[:-4]+ output_tag + ".csv", 'wb') as output_csv: #init output file
			writer = csv.DictWriter(output_csv, fieldnames=self.csv_headers)
			writer.writeheader()
			for row in self.dicter:
				writer.writerow(row)

