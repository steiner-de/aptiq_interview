#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import json 
from urllib.parse import urljoin	
# Modules created for repeatability
from utils import extract_upc



CATEGORY 	= 'humor'
URL 		= 'https://books.toscrape.com/'

if __name__ == '__main__':
	# This program will first start by using beautifulSoup and requests package to identify the categories to load
	# want to extract the following
#		UPC (from the product page)
#						- Title
#						- Price
#						- Image URL
	res 	= requests.get(URL)
	
	h_soup 	= BeautifulSoup(res.text,'html.parser')
	
	# Using the parsed h_soup find the category link 
	link 	= h_soup.find('a',href=re.compile(CATEGORY))
	
	# build the next url
	c_url 	= URL+link.get('href')
	print(f"... Loading the {CATEGORY.upper()} books category at: {c_url}  ...\n")
	#return the category_response
	cat_res = requests.get(c_url)
	
	# load the response for the category
	c_soup 	= BeautifulSoup(cat_res.text,'html.parser')
	book_li = c_soup.find_all('li',class_=re.compile('col'))
	
	for book in book_li:
		# Navigate to the book page to get the UPC information 
		# we can get the url relative path with the same extraction for the title
		a_tag 	= book.find('h3').find('a')
		
		# Load the response with new url that is joined from url_path
		# a_tag.get('href') will pull the relative url path for the specific book
		b_res 	= requests.get(urljoin(c_url,a_tag.get('href')))
		b_soup 	= BeautifulSoup(b_res.text,'html.parser')
		# Extract the title
		title 	= a_tag.get('title')
		# Extract the price
		price 	= book.find('div',class_='product_price').contents
		# Extract the image url 
		""" The alt tag in the image seems to match the title for the book. However I think it is a 
			better system to rely on the actual html text.
		"""
		img_url = book.find('div',class_='image_container').find('img').get('src') 