import csv
from bs4 import BeautifulSoup
# import json
# from urllib import quote
# from urllib import urlopen
# from time import sleep


# def getbudget(file):	# from urllib2 import urlopen
soup = BeautifulSoup(open('movie-budgets.html'))
table = soup.find('table')
headers = [header.text for header in table.find_all('th')]
headers.append('num')
headers.append('date')
headers.append('name')
headers.append('budget')
headers.append('domestic')
headers.append('intl')

rows = []

for row in table.find_all('tr'):
	rows.append([val.text.encode('utf8') for val in row.find_all('td')])

# with open('import_cine.csv', 'wb') as f:
with open('movie-budgets.csv', 'wb') as f:
	writer = csv.writer(f, delimiter='|')
	writer.writerow(headers)

# sorry for all the strip()
	for row in rows:
		if row:
			new_row = []
			# print(row)
			# try:
			num = row[0].strip()
			date = row[1].strip()
			name = row[2].strip()
			budget = row[3].strip()
			new_budget = budget.replace("$", "").replace(",", "")
			domestic = row[4].strip()
			new_domestic = domestic.replace("$", "").replace(",", "")
			intl = row[5].strip()
			new_intl = intl.replace("$", "").replace(",", "")			
			new_row.append(num)
			new_row.append(date)
			new_row.append(name)
			new_row.append(new_budget)
			new_row.append(new_domestic)
			new_row.append(new_intl)
			writer.writerow(new_row)
