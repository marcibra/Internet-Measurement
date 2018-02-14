import sys
import json
import urllib
from datetime import datetime

from ripe.atlas.cousteau import Traceroute, AtlasSource, AtlasCreateRequest

key="e0e39110-95b2-4803-ae8d-b4bd5c042ff4"

traceroute=Traceroute(af=4, target="wikipedia.org", description="test", protocol="TCP",port="443")

source=AtlasSource(type="country", value="lb",requested=8)
#source=AtlasSource(type="probes", value=["4452","13173"])

meas=AtlasCreateRequest(start_time=datetime.utcnow(), key=key,measurements=[traceroute], sources=[source],is_onoff=True)

(succ,resp) = meas.create()

print (succ,resp)

