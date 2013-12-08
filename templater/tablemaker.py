import re
import sys

# text = '''1. Synthesis of Stuff
# 2. More Synthesis of Stuff
# 3. Yet again we synthesized things
# 4. Yay publications
# ''' 

def id_numbers():
	''' Takes number, period, space, and text and returns a list of a number, period, 
	and text 2-item tuples.'''
	with open(sys.argv[1], 'r') as f:
		text = f.read()

	return re.findall(r'([\d]+.) (.+)', text)
	
# tr = '<tr></tr>'


def table(items):
	''' Takes a list of tuples and turns it into a table. '''
	tableStart= '<table>\n\t<thead>\n\t</thead>\n\t<tbody>'
	table = tableStart
	for row in items:
		tableRowStart = '\n\t\t<tr>'
		table += tableRowStart
		for column in row: 
			tableRow = '\n\t\t\t<td>' + column + '</td>'
			table += tableRow
		tableRowEnd = '\n\t\t</tr>\n\t\t'
		table += tableRowEnd
	tableEnd = '\n\t</tbody>\n</table>'
	table += tableEnd
	return table 

if __name__ == '__main__':
	a_table_list = id_numbers()

	completeTable = table(a_table_list)

	with open('tablemade.txt', 'a') as f:
		f.write(completeTable)

