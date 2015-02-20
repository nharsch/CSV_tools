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

	def update(self, CsvTable2, shared_key):
		'''
		csv compare loop
		returns 
		assumes both lsiters are lists of dicts
		'''
		#check if shared key in both tables
		assert shared_key in self.csv_headers
		assert shared_key in CsvTable2.csv_headers

		for header in CsvTable2.csv_headers:
			if header not in self.csv_headers:
				self.csv_headers.append(header)

		for row2 in CsvTable2.dicter:
			in_1 = False
			for row1 in self.dicter:
				if row2.get(shared_key) == row1.get(shared_key):
					row1.update(row2)
					#row1['updated_last'] = now
					in_1 = True
			if not in_1:
				self.dicter.append(row2)

class CsvWalker:
	'''
	creates object that will read input CSV line by line and
	write to output
	'''
	def __init__(self, csv_name, output_tag):
		self.csv_name = csv_name #this is the filename
		self.csv_file = open(csv_name, 'rU') #open file in Universal read line
		self.csv_headers = csv.reader(self.csv_file).next()
		self.DictReader = csv.DictReader(self.csv_file, fieldnames=self.csv_headers)
		self.output_tag = output_tag
		self.output_headers = self.csv_headers[:]

	def start_writer(self):
		self.output_csv = open(self.csv_name[:-4]+ self.output_tag + ".csv", 'wb')
		self.DictWriter = csv.DictWriter(self.output_csv, fieldnames=self.output_headers)
		self.DictWriter.writeheader()


