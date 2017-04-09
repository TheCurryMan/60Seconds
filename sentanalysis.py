import urllib3
import speech_recognition as sr
from textblob import TextBlob
from pydub import AudioSegment
import os

def runSentimentAnalysis(audiourl):
	http = urllib3.PoolManager()
	r = http.request('GET', audiourl, preload_content=False)

	with open("tmp.mp3", 'wb') as out:
		while True:
			data = r.read(100)
			if not data:
				break
			out.write(data)
	r.release_conn()

	aud = AudioSegment.from_mp3("tmp.mp3")
	aud.export("tmp.wav",format="wav")
	r = sr.Recognizer()
	audio = None
	with sr.AudioFile("tmp.wav") as source: 
		audio = r.listen(source)
	txt = r.recognize_google(audio)
	os.remove("tmp.wav")
	os.remove("tmp.mp3")
	return TextBlob(txt).sentiment.polarity

#print(runSentimentAnalysis("api.twilio.com/2010-04-01/Accounts/ACe7c0012d06fc3b85303d8387dffdf672/Recordings/REf18f17cc7638ce9aae10d95dee97bb8c.mp3"))