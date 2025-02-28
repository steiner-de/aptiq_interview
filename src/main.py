#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re

CATEGORY 	= 'humor'
URL 		= 'https://books.toscrape.com/'

if __name__ == '__main__':
	# This program will first start by using beautifulSoup and requests package to identify the categories to load
	
	res 	= requests.get(URL)
	
	h_soup 	= BeautifulSoup(res.text,'html.parser')
	
	# Using the parsed h_soup find the category 
	link 	= h_soup.find('a',href=re.compile(CATEGORY))
	
	# build the next url
	c_url 	= URL+link.get('href')
	print(f"... Loading the {CATEGORY} books category at: {c_url}  ...\n")
	book_res= requests.get(c_url)
	
	c_soup 	= BeautifulSoup(book_res.text,'html.parser')