import csv
from bs4 import BeautifulSoup

def getdata(file):	# from urllib2 import urlopen
	soup = BeautifulSoup(open(file))
	table = soup.find('table')
	headers = []
	headers.append('title')
	headers.append('year')
	headers.append('director')
	headers.append('asl')
	headers.append('imdbcode')
	headers.append('shotnum')
	headers.append('shotlength')
	headers.append('timecode')
	headers.append('shottype')
	rows = []

	for row in table.find_all('tr'):
		rows.append([val.text.encode('utf8') for val in row.find_all('td')])

	# with open('import_cine.csv', 'wb') as f:
	with open( file + '.csv', 'wb') as f:
		writer = csv.writer(f, delimiter='|')
		writer.writerow(headers)

	# sorry for all the strip()

		for row in rows:
			title = row[0].strip()
			yr = row[1].strip()
			director = row[2].strip()
			asl = row[3].strip()		
			imdbcode = row[4].strip()
			timerow = row[5].strip().split('\n')
			for shot in timerow:
				new = shot.strip('\t').split(';')
				shotnum = new[0].strip()
				shotlength = new[1].strip() 
				timecode = new[2].strip()
				try:
				  shottype = new[3].strip()
				except IndexError:
				  shottype = ''
				new_row = []
				new_row.append(title)
				new_row.append(yr)
				new_row.append(director)
				new_row.append(asl)
				new_row.append(imdbcode)
				new_row.append(shotnum)
				new_row.append(shotlength)
				new_row.append(timecode)
				new_row.append(shottype)

				writer.writerow(new_row)
		
getdata("new_mdata.htm")


