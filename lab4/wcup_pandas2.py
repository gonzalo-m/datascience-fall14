import re
import pandas as pd
import numpy as np

with open('worldcup.txt', 'r') as f:
        lines = f.readlines()

country_p = re.compile('([A-Z]{3})')
n_titles_p = re.compile('^\|.*([0-9])\s\(')
year_p = re.compile('\[\[([0-9]{4})')

all_countries = []
row = []
country = ""
num_titles = 0
years = []

count = 0
for l in lines:
	line = l.strip()
	# country
	if re.match('^\|.*\{\{fb\|[A-Z]{3}', line):
		country = country_p.search(line).group(1)
		row.append(country)

	# position and year
	elif re.match('^\|.*[0-9]\s\(', line):
		# print line
		num_titles = int(n_titles_p.search(line).group(1))
		years = year_p.findall(line)
		row.append(num_titles)
		row.append(years)
		count+=1

	# no position
	elif re.match('^\|align', line):
		num_titles = 0
		row.append(num_titles)
		row.append([])
		count+=1

	if (count == 4):
		all_countries.append(row)
		row = []
		count = 0

output = ''
for row in all_countries:
	s = ''
	country = ''
	pos = 1
	for field in row:
		if isinstance(field, int):
			continue

		if isinstance(field, str):
			country += field

		elif isinstance(field, list):
			for year in field:
				s += country + "," + str(year) + "," + str(pos)
				output += s + "\n"
				s = ''
			pos += 1

# done part2 here
with open("wc_output.csv", "w") as csv_file:
    csv_file.write(output)

df = pd.read_csv('wc_output.csv')
print df









