#!/usr/bin/env python

import pandas as pd
import numpy as np
from avro.io import DatumReader
from avro.datafile import DataFileReader

# read file
reader = DataFileReader(open('countries.avro'), DatumReader())
entries = []
for entry in reader:
    entries.append(entry)
reader.close()

# load it into a dataframe 
df = pd.DataFrame(entries)

# count
df = df[df.population > 10000000]
count = len(df)
print count
