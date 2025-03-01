#!/usr/bin/env python3
"""
This file is used to store standalone python methods that can be used outside of the main project
"""
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def extract_upc(category_url, book_page_url):
	"""
	This method will return the contents of a webpage and extract out the UPC information 
	for a given book detail page from the website, toscrape.com
	
	INPUTS: 
		category_url: str
			the category html page url string
		book_page_url: str 
			the relative path to the book page url

	RETURNS: 
		upc_val: str 
			The extracted UPC value for the given book
	"""
	b_res 		= requests.get(urljoin(category_url,book_page_url))
	b_soup 		= BeautifulSoup(b_res.text,'html.parser')
	# The UPC is found in a table so look for all table rows
	tab_tag 	= b_soup.find_all('tr')
	# Loop with break to find the UPC then exit immediately 
	for row in tab_tag:
		if row.find('th').contents[0] == 'UPC':
			# we want to extract out this value for the table details
			upc_val = row.find('td').contents[0]
			break 
	return upc_val
	
	
		