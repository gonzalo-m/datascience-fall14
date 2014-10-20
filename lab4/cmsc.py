import re

with open('cmsc.txt', 'r') as f:
        lines = f.readlines()

all_records = []
sing_record = []
course = ""

# patterns
total_p = re.compile('Total: ([0-9]+)')
open_p = re.compile('Open: ([0-9]+)')
wait_p = re.compile('Waitlist: ([0-9]+)')
days_p = re.compile('^([MTuWThF]+)\s[0-9]')
time_p = re.compile('([0-9]+:[0-9]+[pam]+ - [0-9]+:[0-9]+[pam]+)')
bldg_p = re.compile('([A-Z]{3})\s+([0-9]{4})')

for x in lines:
	line = x.strip()
	if re.match('^\s*$', line):
		continue
	elif re.match('^CMSC[0-9]{3}', line):
		course = line
	elif re.match('^[0-9]{4}', line):
		sing_record = []
		sing_record.append(course)
		sing_record.append(line)
	elif re.match('^[A-Z]{3}\s+[0-9]{4}', line):
		sing_record.append(bldg_p.search(line).groups()[0])
		sing_record.append(bldg_p.search(line).groups()[1])
		all_records.append(sing_record)
	else:
		if re.match('^Seats', line):
			sing_record.append(total_p.search(line).group(1))
			sing_record.append(open_p.search(line).group(1))
			sing_record.append(wait_p.search(line).group(1))
		elif re.match('^([MTuWThF]+)\s[0-9]+:', line):
			sing_record.append(days_p.search(line).group(1))
			sing_record.append(time_p.search(line).group(1))
		else:
			sing_record.append(line)

for row in all_records:
	s = ''
	for field in row:
		s += field + ", "
	print s


