from twilio.rest import Client

account_sid = 'ACc2b1bd25252932ce8b7c21519b5cadfe'
auth_token = 'c49155886ae96cee7e63590ede3960e3'

client = Client(account_sid, auth_token)

twilio_number = '+12058275297'
target_number = input("Please Enter the Pakistani phone number: ")
message_body = input("Please Enter the SMS content: ")

message = client.messages.create(
    body=message_body,
    from_=twilio_number,
    to='+92' + target_number
)

print(message.body)
