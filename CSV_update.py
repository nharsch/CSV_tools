#  takes two like CSV files, updates the second
from CSV_tools import CsvTable 
from sys import argv

script, csv1, csv2, shared_key = argv

table1 = CsvTable(csv1)
table2 = CsvTable(csv2)

table1.update(table2, shared_key)
table1.write_out("_updated")

# def find_deletes(DB_lister):
# 	'''
# 	find any items on OVSDB but not on update
# 	'''
# 	for i, row in enumerate(DB_lister):
# 		if row['last_updated'] != now:
# 			del DB_lister[i]

# def CSV_update(CsvTable1, CsvTable2):
# 	'''
# 	csv compare loop
# 	returns 
# 	assumes both lsiters are lists of dicts
# 	'''
# 	for row2 in CsvTable2.dicter:
# 		in_1 = False
# 		for row1 in CsvTable1.dicter:
# 			if row2['PRODID'] == row1['PRODID']:
# 				row1.update(row2)
# 				#row1['updated_last'] = now
# 				in_1 = True
# 		if not in_1:
# 			CsvTable1.dicter.append(row2)
	# return lister_DB

