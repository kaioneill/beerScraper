from sklearn.feature_extraction.text import TfidfVectorizer

# corpus = ['This is the first document.',
#   'This is the second second document.',
#   'And the third one.',
#   'Is this the first document?',
#   ]




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

print(matches)

#print(vectorizer.vocabulary_)
