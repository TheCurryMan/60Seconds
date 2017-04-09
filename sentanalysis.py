from textblob import TextBlob
from twilio.rest import Client


def runSentimentAnalysis(sid):
	account_sid = "ACa9eca256e7d2b82539a0c6086dc244d7"
	auth_token = "213a8dd83633246a86c5b36361665220"
	client = Client(account_sid, auth_token)

	transcription_sid = sid
	transcription = client.transcriptions(transcription_sid).fetch()
	
	return TextBlob(transcription).sentiment.polarity

#print(runSentimentAnalysis()