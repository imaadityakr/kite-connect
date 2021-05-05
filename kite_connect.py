from kiteconnect import KiteConnect

api_key = open('api_key.text', 'r').read()
api_secret = open('api_secret.text', 'r').read()

# print("api_key : ",api_key)
# print("api_secret : ",api_secret)


kite = KiteConnect(api_key=api_key)

kite.login_url()
# print(kite.login_url())


request_token = open('request_token.text', 'r').read()
# print("request_token : ", request_token)
# print()

data = kite.generate_session(request_token, api_secret=api_secret)
# print(" ------ DATA -------")
# print(data)

kite.set_access_token(data["access_token"])