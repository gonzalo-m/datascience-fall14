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

# Delete row 1
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.RowIndex(column=[],
                  table=0,
                  status="active",
                  drop=False,
                  indices=[0])])))

# Set  split  name to  Countries
w.add(dw.SetName(column=["split"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Countries"],
                 header_row=None))

# Set  split1  name to  Year
w.add(dw.SetName(column=["split1"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Year"],
                 header_row=None))

# Set  split2  name to  Position
w.add(dw.SetName(column=["split2"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Position"],
                 header_row=None))

# Set  Countries  name to  Country
w.add(dw.SetName(column=["Countries"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["Country"],
                 header_row=None))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])

