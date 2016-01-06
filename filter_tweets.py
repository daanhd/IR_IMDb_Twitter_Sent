## Daan Disselhorst
## s1683764
## Information Retrieval 
## Usage: python3 filter_tweets.py

import json
import langid
import unicodedata

def main():
	# geef aan welk bestand moet worden geopend
	with open('big_tweet_file/starwar.txt') as bestand:
		bigTweet = json.load(bestand)

	result = []
	counter = 0
	for tweet in bigTweet:
		# gebruik module langid om te filteren op engelse tweets	
		krijgTweets = langid.classify(tweet['text'])	
		
		# als de tweet engels is, sla dan op in txt bestand
		# filter RT en http
		if krijgTweets[0] == 'en':
			if "http" not in tweet['text'] and "RT" not in tweet['text']:
				counter += 1

				geparsed = unicodedata.normalize('NFKD', tweet['text']).encode('ascii','ignore')
				name = str(counter) + ".txt"
				file = open("test_tweets/starwar"+name, "w")
				file.write(geparsed)
				file.close()
				
				print(geparsed)
				print("====")

	print("------")
	print("counter: " + str(counter))

if __name__ == "__main__":
	main()