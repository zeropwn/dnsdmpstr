#!/usr/bin/env python3

import sys
import json
from dnsdmpstr import dnsdmpstr

print("""
	___  _  _ ____ ___  _  _ _  _ ___  
	|  \ |\ | [__  |  \ |  | |\/| |__] 
	|__/ | \| ___] |__/ |__| |  | |    
""")

dnsdump = dnsdmpstr()

if(len(sys.argv) <= 1):
	sys.exit()
else:
	target = sys.argv[1]
	results = dnsdump.dump(target)
	print(json.dumps(results, indent=1))
