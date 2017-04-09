from flask import Flask, request, redirect, send_from_directory
from twilio.rest import Client
from firebase import firebase
import datetime


app = Flask(__name__, static_folder='static')
# Try adding your own number to this list!
account_sid = "ACe7c0012d06fc3b85303d8387dffdf672"
auth_token = "a3d0ce1a83f3d9ac352c26a95c46f96e"
client = Client(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    from_number = request.values.get('From', None)
    call = client.calls.create(from_number, "+14692086476", url="https://fathomless-oasis-22928.herokuapp.com/call.xml", status_callback="http://fathomless-oasis-22928.herokuapp.com/callback?num="+from_number)


    return "Hello nikhil u boosted ape"

@app.route("/callback", methods=['GET', 'POST'])
def callback():
    print(len(client.recordings.list()))
        # Initialize Firebase Application and get user data
    fb = firebase.FirebaseApplication("https://seconds-8d329.firebaseio.com/", None)
    data = fb.get('/users', None)

    num = str(request.values.get("num"))


    print(num)

    rec2 = client.recordings.list()[0]
    finalTwilioURL = "api.twilio.com" + rec2.uri[:-4] + "mp3"
    print(finalTwilioURL)
    date = datetime.datetime.now().strftime ("%m-%d-%Y")
    if num in data:
        data[num][date] = finalTwilioURL
    else:
        data[num] = {date:finalTwilioURL}





    result = fb.put('', '/users', data)

    return "callback func boiz"



@app.route("/call.xml", methods=['GET', 'POST'])
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(debug=True)


