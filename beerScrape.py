#!/usr/bin/python

import urllib.request
from bs4 import BeautifulSoup as soup
from multiprocessing import Pool


beerLinks = []

url = "https://www.ratebeer.com/top"

def getMainSoup(url):
	req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	html = urllib.request.urlopen(req).read()
	pageSoup = soup(html, "lxml")


	return pageSoup


def getSoup(url):
	req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	html = urllib.request.urlopen(req).read()
	pageSoup = soup(html, "lxml")

	beerSoup = pageSoup
	beerLines = beerSoup.findAll("span", {"id":"_description3"})
	description = beerLines[0].text.strip()
	# descriptions.append(description)

	return ''.join(description)




top50Soup = getMainSoup(url)
lines = top50Soup.findAll("tr")
lines.pop(0)







	#line = lines[0]
def getDescriptions():

	#descriptions = []


	for line in lines:

		beerName = line.a.text
		beerType = line.span.text
		percentContainer = line.findAll("td",{"class":"centered"})
		#percent = percentContainer[1].text
		#rating = percentContainer[2].text
		# print("name: " + beerName)
		# print("type: " + beerType)
		# print("abv: " + percent)
		# print("rating: " + rating)
		beerUrl = url.replace('/top','') + line.a.get('href')
		beerLinks.append(beerUrl)



	return beerLinks



def getNames():

	names = []

	for line in lines:

		beerName = line.a.text
		beerType = line.span.text
		percentContainer = line.findAll("td",{"class":"centered"})
		#percent = percentContainer[1].text
		#rating = percentContainer[2].text


		names.append(beerName)


	return names





# if len(records) > 0:
#     .join(records)
