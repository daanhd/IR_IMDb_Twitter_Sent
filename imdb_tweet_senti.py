## Daan Disselhorst
## s1683764
## Information Retrieval 
## Usage: python imdbRev.py

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.tokenize import *

def word_feats(words):
    return dict([(word, True) for word in words])

def get_senti_tweets(data, name):

    schoneData = data.decode('utf-8')
    
    # tokeniseer zinnen
    zinnen = nltk.tokenize.sent_tokenize(schoneData)

    woorden = []
    for zin in zinnen:
        woorden += nltk.tokenize.wordpunct_tokenize(zin)

    testFeatures = word_feats(woorden)

    # print resultaat vd classificatie
    return name + " : " + classifier.classify(testFeatures)


negLabel = movie_reviews.fileids('neg')
posLabel = movie_reviews.fileids('pos')

negFeat = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negLabel]
posFeat = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posLabel]

# Verdeel de dataset:
# 2/3 om te trainen
# 1/3 om te testen
negCut = len(negFeat)*2/3
posCut = len(posFeat)*2/3

# Maak lijsten voor zowel train als test set
trainFeat = negFeat[:negCut] + posFeat[:posCut]
testFeat = negFeat[negCut:] + posFeat[posCut:]
print 'Van de %d reviews, gebruiken we %d reviews om de classifier te trainen, ' \
      'en de resterende %d reviews om te testen.' % (len(trainFeat) + len(testFeat), len(trainFeat), len(testFeat))

# train de naive bayes classifier met de trainings data!
classifier = NaiveBayesClassifier.train(trainFeat)

# geef de testset aan de getrainde classifier en bereken
# hoeveel juist geclassificeerd is
print 'Accuracy van de classifier:', nltk.classify.util.accuracy(classifier, testFeat)

# Print 10 features met 'meeste' informatie
classifier.show_most_informative_features(10)

#####################################################################

print "\nClassificeer op test data van gekozen films: \n"

#######################################
# Sicario 
########################################

counterPosSic = 0
counterNegSic = 0

# geef aantal tweets in testset als range
for i in range(244):
	i+=1
	# open alle tekstbestanden met tweets
	with open("test_tweets/sicario"+str(i)+".txt", "r") as my_file:
		data = my_file.read().replace('\n',' ')
	
	# tel aantal pos en neg
	if get_senti_tweets(data, "Sicario") == "Sicario : pos":
		counterPosSic += 1
	else:
		counterNegSic += 1

print 'Sicario heeft', counterPosSic, 'positieve en',counterNegSic,'negatieve tweets'


#######################################
# Star Wars 
#######################################

counterPosStar = 0
counterNegStar = 0

# geef aantal tweets in testset als range
for i in range(178):
	i+=1
	# open alle tekstbestanden met tweets
	with open("test_tweets/starwar"+str(i)+".txt", "r") as my_file:
		data = my_file.read().replace('\n',' ')
	
	# tel aantal pos en neg
	if get_senti_tweets(data, "Star Wars") == "Star Wars : pos":
		counterPosStar += 1
	else:
		counterNegStar += 1

print 'Star Wars heeft', counterPosStar, 'positieve en',counterNegStar,'negatieve tweets' 

#######################################
# Alvin and the Chipmunks: The Road Chip 
#######################################

counterPosChip = 0
counterNegChip = 0

# geef aantal tweets in testset als range
for i in range(179):
	i+=1
	# open alle tekstbestanden met tweets
	with open("test_tweets/chipmunks"+str(i)+".txt", "r") as my_file:
		data = my_file.read().replace('\n',' ')
	
	# tel aantal pos en neg
	if get_senti_tweets(data, "Chipmunks") == "Chipmunks : pos":
		counterPosChip += 1
	else:
		counterNegChip += 1

print 'Chipmunks heeft', counterPosChip, 'positieve en', counterNegChip, 'negatieve tweets'






