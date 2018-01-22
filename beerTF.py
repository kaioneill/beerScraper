from sklearn.feature_extraction.text import TfidfVectorizer
import beerScrape as scrape
from operator import itemgetter
from multiprocessing import Pool




url = "https://www.ratebeer.com/top"

print('\n')
print("loading beer info...")
print('\n')

# scrape.getMainSoup(url)
# scrape.getDescriptions()
# names = scrape.getNames()
#
#
#
#
# with Pool(10) as p:
# 	records = p.map(scrape.getSoup, scrape.beerLinks)
#
# descs = records
#
# for j in range(len(descs)):
# 	descs[j] = descs[j].lower()
# 	descs[j] = descs[j].replace(',','')
# 	descs[j] = descs[j].replace('.','')

names = ['beer1', 'beer2']

query = 'i like coffee and sweet beer'
#query = input('what qualities do you look for in a beer?\n')
print('\n')

#arr = [query]
arr = []

descs = ['Pliny the Younger was Pliny the Elder’s nephew, in the case of this beer, the "Younger" is a triple IPA. Pliny the Younger is hopped three times more than our standard IPA, and is dry hopped four different times.', 'This beer is the real McCoy. Barrel aged and crammed with coffee, none other will stand in it’s way. Sought out for being delicious, it is notoriously difficult to track down. If you can find one, shoot to kill, because it is definitely wanted... dead or alive.']


for i in descs:
    arr.append(i)

    #print(arr)


vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(arr)

# print(vectorizer.vocabulary_['pliny'])

# print(vectorizer.get_feature_names()[27])



for i in range(1, tfidf.shape[1]):
	weight = tfidf[(1,i)]
	if(weight < .1 and weight > 0.0):
		print(weight)


tempNums = vectorizer.transform([query]).toarray()
tempList = []

#print(tempNums)

for i in range(len(tempNums)):
    if tempNums[i].any() != 0:
        tempList.append([i, tempNums[i]])


#print(len(tempList))

for i in range(len(tempList)):
    temp = int(tempList[i][0])
    #print(names[temp])
    #print('\n')


sim = tfidf * tfidf.T
matches = sim.toarray()[0]

#matches = matches[1:]

#print(matches)




# nameCount = []
#
# for i in range(len(names)):
#     temp = [matches[i], names[i]]
#     nameCount.append(temp)
#
#
# nameCount = sorted(nameCount, key=itemgetter(0), reverse=True)
#
# #print(nameCount)
#
#
#
# q = False
# for item in nameCount:
#     if item[0] != 0:
#         print(item[1])
#         q = True
#     else: break
#
# if not q: print("no matches, sorry")


print('\n')
