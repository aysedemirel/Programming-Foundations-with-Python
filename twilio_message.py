from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Axxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "####"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+9055555555",  # your number
    from_="+133333333", # twilio number
    body="Hello from Python!")

print(message.sid)

# to get a twilio number:
# 1. create a twilio account
# 2. from dashboard select "phone numbers"
# 3. if you want a free number, select "get started"
# 4. select "get your first twilio number"
# 5. twilio will give you a free and random number
# 6. for now, there isn't an option for a number that its location is from Turkey
