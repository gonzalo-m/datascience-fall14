from wrangler import dw
import sys

if(len(sys.argv) < 3):
	sys.exit('Error: Please include an input and output file.  Example python script.py input.csv output.csv')

w = dw.DataWrangler()

# Split data repeatedly on newline  into  rows
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on="\n",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character=None))

# Split data repeatedly on ','
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on=",",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character=None))

# Set  split  name to  Course_No.
w.add(dw.SetName(column=["split"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Course_No."],
                 header_row=None))

# Set  split1  name to  Section No.
w.add(dw.SetName(column=["split1"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Section No."],
                 header_row=None))

# Set  split2  name to  Instructor
w.add(dw.SetName(column=["split2"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Instructor"],
                 header_row=None))

# Set  split3  name to  Seats
w.add(dw.SetName(column=["split3"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Seats"],
                 header_row=None))

# Set  split4  name to  Open
w.add(dw.SetName(column=["split4"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Open"],
                 header_row=None))

# Set  split5  name to  Waitlist
w.add(dw.SetName(column=["split5"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Waitlist"],
                 header_row=None))

# Extract from split6 on ' any number : any number  any lowercase word  -  any number : any number  any lowercase word '
w.add(dw.Extract(column=["split6"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="\\d+:\\d+[a-z]+ - \\d+:\\d+[a-z]+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Set  extract  name to  Time
w.add(dw.SetName(column=["extract"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Time"],
                 header_row=None))

# Set  split6  name to  Days
w.add(dw.SetName(column=["split6"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Days"],
                 header_row=None))

# Cut from Days on ' any number : any number  any lowercase word  -  any number : any number  any lowercase word '
w.add(dw.Cut(column=["Days"],
             table=0,
             status="active",
             drop=False,
             result="column",
             update=True,
             insert_position="right",
             row=None,
             on="\\d+:\\d+[a-z]+ - \\d+:\\d+[a-z]+",
             before=None,
             after=None,
             ignore_between=None,
             which=1,
             max=1,
             positions=None))

# Extract from split7 on ' any number '
w.add(dw.Extract(column=["split7"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="\\d+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Set  extract  name to  Room No.
w.add(dw.SetName(column=["extract"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Room No."],
                 header_row=None))

# Set  split7  name to  Bldg.
w.add(dw.SetName(column=["split7"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Bldg."],
                 header_row=None))

# Extract from Bldg. on ' any word '
w.add(dw.Extract(column=["Bldg."],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on="[a-zA-Z]+",
                 before=None,
                 after=None,
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Drop Bldg.
w.add(dw.Drop(column=["Bldg."],
              table=0,
              status="active",
              drop=True))

# Set  extract  name to  Bldg.
w.add(dw.SetName(column=["extract"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Bldg."],
                 header_row=None))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])

