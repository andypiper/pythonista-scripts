import ui
import base64
import requests


def getInput(v, field):
	return v[field].text


def getBearerToken(sender):
	client_key = getInput(sender.superview, "consumerKey")
	client_secret = getInput(sender.superview, "consumerSecret")

	key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
	b64_encoded_key = base64.b64encode(key_secret)
	b64_encoded_key = b64_encoded_key.decode('ascii')

	auth_url = 'https://api.twitter.com/oauth2/token'

	auth_headers = {
		'Authorization': 'Basic {}'.format(b64_encoded_key),
		'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
	}

	auth_data = {'grant_type': 'client_credentials'}

	auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

	access_token = auth_resp.json()['access_token']

	sender.superview["bearerToken"].text = access_token


ui.load_view('bearertoken').present()

