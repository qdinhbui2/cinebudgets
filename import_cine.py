import csv
from bs4 import BeautifulSoup
# import json
# from urllib import quote
# from urllib import urlopen
# from time import sleep


# API_URL = "http://www.omdbapi.com/?r=json&i=%s"
# print(API_URL)

# class APIError(Exception):
# 	pass

# def search(code):
# 	code = code.encode("utf-8")
# 	url = API_URL % quote(code)
# 	data = urlopen(url).read().decode("utf-8")
# 	sleep(0.1)
# 	values = []
# 	# print(data)
# 	data = json.loads(data)
# 	if data.get("Response") == "False":
# 		pass
# 		# raise APIError(data.get("Error", "Unknown error"))
# 	iden = data['imdbID']
# 	rating = data['imdbRating']
# 	votes = data['imdbVotes']
# 	genre = data['Genre']
# 	awards = data['Awards']
# 	values.append(iden)
# 	values.append(rating)
# 	values.append(votes)
# 	values.append(genre)
# 	values.append(awards)
# 	return values


def getdata(file):	# from urllib2 import urlopen
	soup = BeautifulSoup(open('/Users/QuoctrungBui/Dropbox/' + file))
	table = soup.find('table')
	headers = [header.text for header in table.find_all('th')]
	headers.append('rating')
	headers.append('votes')
	headers.append('genre')
	headers.append('awards')
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
			#pull data from imdb
			imdbcode = row[4].strip()
			# no imbd data
			# imdbdata = search(imdbcode) 
			# rating = imdbdata[1].strip()		
			# votes = imdbdata[2].strip()		
			# genre = imdbdata[3].strip()		
			# awards = imdbdata[4].strip()		
			# print(imdbdata)
			testrow = row[5].strip().split('\n')
			# print testrow
			for shot in testrow:
				new = shot.strip('\t').split(';')
				shotnum = new[0].strip()
				shotlength = new[1].strip() 
				timecode = new[2].strip()
				try:
				  shottype = new[3].strip()
				except IndexError:
				  shottype = ''
				new_row = []
				# new_row = row[:5]
				# new_row.append(new)
				new_row.append(title)
				new_row.append(yr)
				new_row.append(director)
				new_row.append(asl)
				new_row.append(imdbcode)
				new_row.append(shotnum)
				new_row.append(shotlength)
				new_row.append(timecode)
				new_row.append(shottype)
				# new_row.append(rating)
				# new_row.append(votes)
				# new_row.append(genre)
				# new_row.append(awards)

				writer.writerow(new_row)
		
getdata("new_mdata.htm")


