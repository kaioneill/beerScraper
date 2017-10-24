#!/usr/bin/python

import beerScrape as scrape
import operator
from multiprocessing import Pool

# from multiprocessing import Pool

# p = Pool(10)
# records = p.map(parse, getDescriptions())

url = "https://www.ratebeer.com/top"


print("loading beer info...")

scrape.getMainSoup(url)
scrape.getDescriptions()


with Pool(10) as p:
	records = p.map(scrape.getSoup, scrape.beerLinks)



descs = records
#descs = ['this is coffee, it is good','this is not']


for j in range(len(descs)-1):
	descs[j] = descs[j].lower()
	descs[j] = descs[j].replace(',','')
	descs[j] = descs[j].replace('.','')
	descs[j] = descs[j].split(' ')



#descs[0] = descs[0].split(' ')

#print(descs[0][0])

wordCount = [0] * len(descs)


def typeStuff():


	userDesc = input("enter a few words to describe beer that you like\n")
	userDesc = userDesc.lower()
	userWords = userDesc.split(' ')

	#print('\n')



	for w in range(len(descs)-1):
		for userWord in range(len(userWords)-1):
			for beerWord in userWords:
				if userWord == beerWord:
					wordCount[w] += 1




	print('\n')

	print(len(descs))


	names = scrape.getNames()

	# together = zip(nums, wordCount)
	# sorted_together =  sorted(together)

	# wordCount = [x[0] for x in sorted_together]
	# names = [x[1] for x in sorted_together]

	k = 0
	q = False
	for count in wordCount:
		if count > 0:
			print(names[k])
			q = True
		k += 1

	if not q: print("no matches, sorry")

	#index, value = max(enumerate(wordCount), key=operator.itemgetter(1))

	print('\n')
	#print(wordCount)
	return
typeStuff()




while input('again? y/n\n') == 'y':
	wordCount = [0] * len(descs)
	names = []
	typeStuff()
