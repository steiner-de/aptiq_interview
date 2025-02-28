#!/usr/bin/env python3
"""
This module is used as wrapper methods on the requests python library. 
"""

def get_request(url,bearer_token=None, username=None, password=None, hdr=None, body=None):
	"""
	
	
	INPUTS: 
		url: str (not null)
			The url is the url value that will be passed to the package to return
		
	"""
	import requests
	if bearer_token:
		print("Use of a bearer token has been provided.")
		