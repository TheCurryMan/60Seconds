from textblob import TextBlob

def runSentimentAnalysis(text):
	blob = TextBlob(text)	
	return blob.sentiment.polarity
