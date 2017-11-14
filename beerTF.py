from sklearn.feature_extraction.text import TfidfVectorizer
import beerScrape as scrape
from operator import itemgetter

#names = scrape.getNames()

names = ['beer1', 'beer2']


query = 'I like coffee and sour'

arr = [query]

beer = ['This beer is the real McCoy. Barrel aged and crammed with coffee, none other will stand in it’s way. Sought out for being delicious, it is notoriously difficult to track down. If you can find one, shoot to kill, because it is definitely wanted... dead or alive.', 'Pliny the Younger was Pliny the Elder’s nephew, in the case of this beer, the "Younger" is a triple IPA. Pliny the Younger is hopped three times more than our standard IPA, and is dry hopped four different times.']


for i in beer:
    arr.append(i)

#print(arr)

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(arr)
vals = tfidf.toarray()

sim = tfidf * tfidf.T
matches = sim.toarray()[0]

matches = matches[1:]

print(matches)




nameCount = []

for i in range(len(names)-1):
    temp = [matches[i], names[i]]
    nameCount.append(temp)


nameCount = sorted(nameCount, key=itemgetter(0), reverse=True)



print(nameCount)
