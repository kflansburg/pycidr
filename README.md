# Installation

Install python dependencies:
```
pip install -r requirements
```

Retrieve latest data and build CIDR maps of each (Takes a few minutes)
```
make fetch
```

# Usage
```
>>> from pycidr.cidr import CIDR
>>> A = CIDR()
>>> A.load("data/ASNMAP")
>>> A['8.8.8.8']
(3356, 'LEVEL3 - Level 3 Communications, Inc., US', '8.0.0.0/8')
>>> G = CIDR()
>>> G.load("data/GEOMAP")
>>> G['8.8.8.8']
('North America', 'United States', 'California', 'Mountain View', '8.8.8.0/24', 37.386, -122.0838, 1000)
>>>
```

ASN CIDRs return (ASN Number, ASN Name, Network)

GEO CIDRs return (Continent, Country, State, City, Network, Latitude, Longitude, Accuracy (m))
