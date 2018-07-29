#!/usr/bin/python
import sys
import re
fault = []
for line in sys.stdin:
    data = re.findall(r'"([^"]*)"',line)
    # Below are the error cases in which the records need to be skipped
    if (data[0]=="ID") or (len(data)!=7):
        fault.append(data)
        continue
    airportType = data[1]
    # Below step is taken, by the assumption that no field value has a tab in it
    print "{0}\t{1}".format(airportType,1)
