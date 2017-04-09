from flask import Flask, request, redirect, send_from_directory
from twilio.rest import Client
from firebase import firebase
import datetime
from textblob import TextBlob


app = Flask(__name__, static_folder='static')
# Try adding your own number to this list!
account_sid = "ACa9eca256e7d2b82539a0c6086dc244d7"
auth_token = "213a8dd83633246a86c5b36361665220"
client = Client(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    to_number = request.values.get('From', None)
    call = client.calls.create(to_number, "+15107688341", url="https://fathomless-oasis-22928.herokuapp.com/call.xml") #status_callback="http://fathomless-oasis-22928.herokuapp.com/transcribecallback?num="+to_number)
    return "Server for 60Seconds"

# @app.route("/callback", methods=['GET', 'POST'])
# def callback():
#     #print(len(client.recordings.list()))
#         # Initialize Firebase Application and get user data
#     fb = firebase.FirebaseApplication("https://seconds-8d329.firebaseio.com/", None)
#     data = fb.get('/users', None)
#     num = "+" + str(request.values.get("num"))[1:]
#     #print(num)
#     rec2 = client.recordings.list()[0]
#     finalTwilioURL = "api.twilio.com" + rec2.uri[:-4] + "mp3"
#     #print(finalTwilioURL)
#     date = datetime.datetime.now().strftime ("%m-%d-%Y")
#     if num in data:
#         data[num][date] = finalTwilioURL  
#     else:
#         data[num] = {date:finalTwilioURL}

#     result = fb.put('', '/users', data)

#     return "callback func boiz"

@app.route("/transcribecallback", methods=['GET','POST'])
def transcribecallback():
    fb = firebase.FirebaseApplication("https://seconds-8d329.firebaseio.com/", None)
    data = fb.get('/users', None)
    rec2 = client.recordings.list()[0]
    finalTwilioURL = "api.twilio.com" + rec2.uri[:-4] + "mp3"

    text = str(request.values.get("TranscriptionText"))
    date = datetime.datetime.now().strftime("%m-%d-%Y")
    sent = TextBlob(text).sentiment.polarity
    print(request.values)
    num = str(request.values.get("To"))
    print(num)
    if num in data:
        data[num][date]["sent"] = sent
        data[num][date]["url"] = finalTwilioURL
    else:
        data[num][date] = {"sent":sent, "url": finalTwilioURL}

    result = fb.put('', '/users', data)

    return "Callback function"

@app.route("/call.xml", methods=['GET', 'POST'])
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    app.run(debug=True)


