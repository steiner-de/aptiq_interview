#!/usr/bin/env python3
"""
This module is used as wrapper methods on the requests python library. 
"""

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
	
		