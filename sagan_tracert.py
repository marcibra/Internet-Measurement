import sys
import json
import urllib
from datetime import datetime
from ripe.atlas.sagan import Result, TracerouteResult

from ripe.atlas.cousteau import AtlasLatestRequest

kwargs={"msm_id":11304100}

is_succ, results=AtlasLatestRequest(**kwargs).create()

#if is_succ:
#	print(results)

for result in results:
	print(Result.get(result))
	tracert=TracerouteResult(result)
	print(tracert.total_hops)
	print(tracert.ip_path)
		





