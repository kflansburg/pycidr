import csv
from cidr import CIDR
import sys

if len(sys.argv)<4:
    print "python parsegeo.py <geo_loc.csv> <geo_ip.csv> <output>"

f = open(sys.argv[1])
R = csv.reader(f, skipinitialspace=True)
R.next()
print "Reading Cities"
LOCs = {}
for l in R:
    try: 
        geo_id, _, _, cont, _, country, _, state, _, _, city, _, _   = l
    except ValueError:
        print l

    geo_id = int(geo_id)
    if geo_id in LOCs: print "Colision!"
    LOCs[geo_id] = (cont, country, state, city)
f.close()

print "Reading Networks"
f = open(sys.argv[2])
R = csv.reader(f, skipinitialspace=True)
R.next()
N = 10
LOC_o = CIDR()
F = 0
for l in R:
    try:
        ipn, geo_id, _, _, _, _, _, lat, lon, rad = l
        geo_id = int(geo_id)
        d = LOCs[geo_id]+(ipn, float(lat), float(lon), int(rad),)
        LOC_o[ipn] = d
    except Exception as e:
        F+=1
f.close()
print "%d Networks missing GEOID"%(F)

LOC_o.save(sys.argv[3])
