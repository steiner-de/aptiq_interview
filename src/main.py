#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import json 
from urllib.parse import urljoin	
# Modules created for repeatability
from utils import extract_book_details


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
		# Created a method to extract out this information
		book_dict 	= extract_book_details(book,c_url)
		if 'dict_list' in locals():
			dict_list.append(book_dict)
		else:
			dict_list = [book_dict]
		del book_dict
		
	# print the json dumps. The price is in a specific encoding. The code needs to translate this encoding
	print(json.dumps(dict_list, ensure_ascii=False).encode(cat_res.encoding).decode('latin-1'))
	