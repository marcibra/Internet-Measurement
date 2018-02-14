import sys
import json
import urllib

from ripe.atlas.cousteau import Probe, ProbeRequest 
filters = {"country_code": "LB"}
probes = ProbeRequest(**filters)

for probe in probes:
    print(probe["id"])
    i=probe["id"]
    p=Probe(id=i)
    print(p.tags) 
   

# Print total count of found probes
#print(probe["count"])
