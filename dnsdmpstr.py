#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

class dnsdmpstr():
	"""
	initialization
	this is where the csrf token is fetched & set
	"""
	def __init__(self):
		self.headers = {
			"Referer":"https://dnsdumpster.com"
		}
		r = requests.get("https://dnsdumpster.com", headers=self.headers)
		doc = BeautifulSoup(r.text.strip(), "html.parser")
		try:
			# locate the csrf token
			tag = doc.find("input", {"name":"csrfmiddlewaretoken"})
			self.csrftoken = tag['value']
			# to avoid a 403, the csrftoken cookie has to be set,
			# along with the referer.
			self.headers = {
			"Referer":"https://dnsdumpster.com",
			"Cookie": "csrftoken={0};".format(self.csrftoken)
			}
		except:
			pass

	"""
	filter function for the record tables
	note: make sure txt records are filtered with record_type=1
	      this is because it uses different formatting
	"""
	def _clean_table(self, table, record_type=0):
		retval = {}
		if record_type==1:
			for idx,tag in enumerate(table.find_all('td')):
				retval[idx] = tag.string
		for idx,tag in enumerate(table.find_all('td', { 'class':'col-md-4'})):
			clean_name = tag.text.replace('\n', '')
			clean_ip = tag.a['href'].replace('https://api.hackertarget.com/reverseiplookup/?q=', '')
			retval[idx] = { 'ip':clean_ip, 'host':clean_name}
		return retval

	"""
	return information on given target
	this is where all the records are cleaned and stored
	"""
	def dump(self, target):
		retval = {}
		data = {"csrfmiddlewaretoken": self.csrftoken, "targetip": target}
		r = requests.post("https://dnsdumpster.com", headers=self.headers, data=data)
		doc = BeautifulSoup(r.text.strip(), "html.parser")
		tables = doc.find_all('table')
		try:
			retval['dns'] = self._clean_table(tables[0])
			retval['mx'] = self._clean_table(tables[1])
			retval['txt'] = self._clean_table(tables[2], 1)
			retval['host'] = self._clean_table(tables[3])
			return retval
		except:
			return False

	"""
	execute host search on hackertarget api
	"""
	def hostsearch(self, target):
		try:
			# accepts a domain name
			r = requests.get("https://api.hackertarget.com/hostsearch/?q={}".format(target))
			return(r.text)
		except:
			return("An error occurred.")
	"""
	execute reversedns search on hackertarget api
	"""
	def reversedns(self, target):
		try:
			# accepts an IP, IP range or domain name.
			r = requests.get("https://api.hackertarget.com/reversedns/?q={}".format(target))
			return(r.text)
		except:
			return("An error occurred.")
	"""
	execute dnslookup on hackertarget api
	"""
	def dnslookup(self, target):
		try:
			# accepts a domain name
			r = requests.get("https://api.hackertarget.com/dnslookup/?q={}".format(target))
			return(r.text)
		except:
			return("An error occurred.")

	"""
	grab page links from hackertarget api
	"""
	def pagelinks(self, target):
		try:
			# accepts a domain name / ip
			r = requests.get("https://api.hackertarget.com/pagelinks/?q={}".format(target))
			return(r.text)
		except:
			return("An error occurred.")

	"""
	grab returned http headers from page using hackertarget api
	"""
	def httpheaders(self, target):
		try:
			# accepts a domain name
			r = requests.get("https://api.hackertarget.com/httpheaders/?q={}".format(target))
			return(r.text)
		except:
			return("An error occurred.")
