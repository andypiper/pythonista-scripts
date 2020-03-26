# Provide a Tweet ID, displays it as a web embed in a UIWebView
import requests
import json
import ui

def getInput(v, field):
	return v[field].text

def showTweet(sender):
	tweetId = getInput(sender.superview, "tweetId")
	
	embReqUrl = 'https://publish.twitter.com/oembed.json?url=https://twitter.com/Twitter/status/'+tweetId
	embResp = requests.get(embReqUrl)
	
	if (embResp.status_code == 200):
		resp_dict = embResp.json()
		htmlpage = resp_dict['html']
		
		v = ui.WebView(name="Tweet", scales_page_to_fit=True)
		v.load_html(htmlpage)
		v.size_to_fit()
		v.present()
		
ui.load_view('oembed').present()
