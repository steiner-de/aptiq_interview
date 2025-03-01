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

def extract_book_details(book_details,current_url,get_upc=True,get_title=True,get_img=True,get_price=True):
	# Navigate to the book page to get the UPC information 
	# we can get the url relative path with the same extraction for the title
	a_tag 					= book_details.find('h3').find('a')		
	# Load the response with new url that is joined from url_path
	# a_tag.get('href') will pull the relative url path for the specific book
	if get_upc:
		# Create the dictionary object and add the keys to it.
		book_dict 				= {'upc':extract_upc(current_url, a_tag.get('href'))}
	if get_title:
		# Extract the title
		book_dict['title'] 		= a_tag.get('title')
	if get_img:
		# Extract the price
		book_dict['image_url'] 	= book_details.find('div',class_='image_container').find('img').get('src') 
		# Extract the image url 
		""" The alt tag in the image seems to match the title for the book. However I think it is a 
			better system to rely on the actual html text.
		"""
	if get_price:
		# Price is encoded and needs to be corrected to better represent the pound currency 
		# This will be further encoded and decoded in the json.dumps statement
		book_dict['price'] 		= book_details.find('p',class_='price_color').contents[0]
	print(f'Finished loading {book_dict["title"]}')
	return book_dict
	
	
		