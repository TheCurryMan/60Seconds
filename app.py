from flask import Flask, request
import twilio.twiml
from twilio.rest import Client



app = Flask(__name__)
# Try adding your own number to this list!
account_sid = "ACe7c0012d06fc3b85303d8387dffdf672"
auth_token = "a3d0ce1a83f3d9ac352c26a95c46f96e"
client = Client(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    print("NIKHIL U BOOSTED APE")

    #Getting actual message from user
    body = request.values.get('Body', None)

    #Getting any image the user might have sent
    img_url = request.values.get('MediaUrl0', None)

    #Getting the from number from the user
    from_number = request.values.get('From', None)

    #Gets the message that's returned back to the user
    message = "Hello"

    #Sends the message back
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


