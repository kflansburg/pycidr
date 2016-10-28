clean:
	rm -rf data/*

fetch: download parse

download:
	mkdir -p data
	# Geolocation Informaion
	wget -P data/ http://geolite.maxmind.com/download/geoip/database/GeoLite2-City-CSV.zip
	unzip -d data/ data/GeoLite2-City-CSV.zip
	# ASN Information
	wget -P data/ http://thyme.apnic.net/current/data-raw-table
	wget -P data/ http://thyme.apnic.net/current/data-used-autnums

parse:
	python pycidr/parsegeo.py data/GeoLite2-City-CSV*/GeoLite2-City-Locations-en.csv data/GeoLite2-City-CSV_*/GeoLite2-City-Blocks-IPv4.csv data/GEOMAP
	python pycidr/parseasn.py data/data-used-autnums data/data-raw-table data/ASNMAP	

