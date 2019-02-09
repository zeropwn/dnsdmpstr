#!/usr/bin/env python3

import sys
import json
import argparse
from dnsdmpstr import dnsdmpstr

print("""
	___  _  _ ____ ___  _  _ _  _ ___  
	|  \ |\ | [__  |  \ |  | |\/| |__] 
	|__/ | \| ___] |__/ |__| |  | |    

	./ddump.py hackerone.com --all
""")

parser = argparse.ArgumentParser()
parser.add_argument('-u', help="target domain")
parser.add_argument('-a', help="host search (DNS A Record lookup)", action="store_true")
parser.add_argument('-r', help="reverse dns lookup (accepts IP, IP range or domain name)", action="store_true")
parser.add_argument('-d', help="dns lookup", action="store_true")
parser.add_argument('-dd', help="classical dns dump format", action="store_true")
parser.add_argument('--links', help="grab page links from url", action="store_true")
parser.add_argument('--headers', help="grab http headers from url", action="store_true")
parser.add_argument('--all', help="grab all information available", action="store_true")
args = parser.parse_args()

dnsdump = dnsdmpstr()

if(args.u):
	target = args.u
	if(args.dd):
		print(json.dumps(dnsdump.dump(target), indent=1))
	if(args.a):
		print(dnsdump.hostsearch(target))
	if(args.r):
		print(dnsdump.reversedns(target))
	if(args.d):
		print(dnsdump.dnslookup(target))
	if(args.links):
		print(dnsdump.pagelinks(target))
	if(args.headers):
		print(dnsdump.httpheaders(target))
	if(args.all):
		print(json.dumps(dnsdump.dump(target), indent=1))
		print(dnsdump.hostsearch(target))
		print(dnsdump.reversedns(target))
		print(dnsdump.dnslookup(target))
		print(dnsdump.pagelinks(target))
		print(dnsdump.httpheaders(target))
