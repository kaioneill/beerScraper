from sklearn.feature_extraction.text import TfidfVectorizer
import beerScrape as scrape
from operator import itemgetter
from multiprocessing import Pool




url = "https://www.ratebeer.com/top"

print('\n')
print("loading beer info...")
print('\n')

scrape.getMainSoup(url)
scrape.getDescriptions()
names = scrape.getNames()




with Pool(10) as p:
	records = p.map(scrape.getSoup, scrape.beerLinks)

descs = records

for j in range(len(descs)):
	descs[j] = descs[j].lower()
	descs[j] = descs[j].replace(',','')
	descs[j] = descs[j].replace('.','')

# names = ['beer1', 'beer2']

# query = 'i like coffee and sweet beer'
# query = input('what qualities do you look for in a beer?\n')
# print('\n')

#arr = [query]
arr = []

# descs = ['Pliny the Younger was Pliny the Elder’s nephew, in the case of this beer, the "Younger" is a triple IPA. Pliny the Younger is hopped three times more than our standard IPA, and is dry hopped four different times.', 'This beer is the real McCoy. Barrel aged and crammed with coffee, none other will stand in it’s way. Sought out for being delicious, it is notoriously difficult to track down. If you can find one, shoot to kill, because it is definitely wanted... dead or alive.']



for i in descs:
    arr.append(i)

    #print(arr)


vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(arr)

# print(vectorizer.vocabulary_['pliny'])



clean = []
newDescs = []



for j in range(len(descs)-1):
	tempDesc = ''
	for i in range(0, tfidf.shape[1]):
		weight = tfidf[(j,i)]
		tempName = vectorizer.get_feature_names()[i]
		if(weight < .1 and weight > .07 and ((' ' + tempName + ' ') in descs[j])):
			# print(tempName)
			tempDesc += (tempName + ' ')
			clean.append((i, tempName, weight))
	newDescs.append(tempDesc)



# print(tfidf.toarray())
# print(newDescs)
descs = newDescs
# print(vectorizer.get_feature_names()[165])



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
