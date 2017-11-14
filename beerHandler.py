#!/usr/bin/python

import beerScrape as scrape
import operator
from multiprocessing import Pool
from operator import itemgetter



url = "https://www.ratebeer.com/top"


print("loading beer info...")

scrape.getMainSoup(url)
scrape.getDescriptions()


with Pool(10) as p:
	records = p.map(scrape.getSoup, scrape.beerLinks)



descs = records
#descs = ['this is coffee, it is good','this is not']


for j in range(len(descs)):
	descs[j] = descs[j].lower()
	descs[j] = descs[j].replace(',','')
	descs[j] = descs[j].replace('.','')
	descs[j] = descs[j].split(' ')





wordCount = [0] * len(descs)


def typeStuff():


	userDesc = input("enter a few words to describe beer that you like\n")
	userDesc = userDesc.lower()
	userWords = userDesc.split(' ')

	#print('\n')


	w = 0
	for desc in descs:
		for userWord in userWords:
			for beerWord in desc:
				if userWord == beerWord:
					wordCount[w] += 1
		w += 1




	print('\n')



	names = scrape.getNames()



	nameCount = []

	for i in range(len(names)-1):
		temp = [wordCount[i], names[i]]
		nameCount.append(temp)


	nameCount = sorted(nameCount, key=itemgetter(0), reverse=True)

	#print(nameCount)

	q = False
	for item in nameCount:
		if item[0] != 0:		#if count isn't zero
			print(item[1])		#print the name
			q = True
		else: break

	if not q: print("no matches, sorry")


	print('\n')
	#print(wordCount)
	return
typeStuff()




while input('again? y/n\n') == 'y':
	wordCount = [0] * len(descs)
	names = []
	typeStuff()
