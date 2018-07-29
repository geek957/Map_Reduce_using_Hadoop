import sys

Airports = 0
prvkey = Null
for line in sys.stdin:
    data = line.strip().split("\t")
    data=data.split(" ")
    # Below are the error cases in which the records need to be skipped
    if (len(data) == 2):
        prsnt_type,value = data
        if prvkey and (prvkey!=prsnt_type):
            print prvkey,Airports
            # print "{0}\t{1}".format(prvkey,Airports)
            Airports = 0
        Airports += int(val)
        prvkey = prsnt_type
