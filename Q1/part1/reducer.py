#!/usr/bin/python
import sys

Airports = 0
prvkey = None
#oldkey_country = None
#oldkey_type = None
for line in sys.stdin:
    data = line.strip().split("\t")
    # Below are the error cases in which the records need to be skipped
    if (len(data) == 2):
        prsnt_key,val = data
        if prvkey and (prvkey!=prsnt_key):
            print "{0}\t{1}".format(prvkey,Airports)
            Airports = 0
        Airports += int(val)
        prvkey = prsnt_key
        
