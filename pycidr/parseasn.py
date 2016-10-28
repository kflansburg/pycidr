from cidr import CIDR
import sys

if len(sys.argv)<4:
    print "python parseasn.py <data-used-autnums> <data-raw-table> <output>"

f = open(sys.argv[1],'r')
print "Reading AS Names"
ASN_names = {}
for l in f:
    data = l.strip().split(" ")
    n = int(data[0])
    name = " ".join(data[1:])
    ASN_names[n] = name
f.close()
print "%d AS names found"%(len(ASN_names.keys()))

def pretty(d, indent=0):
   for key, value in d.iteritems():
      print '  ' * indent + str(key)
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print '  ' * (indent+1) + str(value)
 
f = open(sys.argv[2],'r')
N = 0
U = 0
ASNs = CIDR()
print "Reading AS IP Sets"

for l in f:
    N+=1
    data = l.strip().split("\t")
    cidr = data[0]
    n = int(data[1])
    try:
        name = ASN_names[n]
    except KeyError:
        U+=1
        name = "Unknown"
    ASNs[cidr] = (n, name, str(cidr))
f.close()

print "%d CIDRs Found"%(N,)
print "%d Unrecognized AS Numbers"%(U,)

ASNs.save(sys.argv[3])

