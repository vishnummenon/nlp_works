from bs4 import BeautifulSoup
from text_summarizer import FrequencySummarizer
import requests
from urllib.request import Request, urlopen

def getTextFromURL(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	print (text)
	return text

def urlfetch(url):
	f = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
	myfile = urlopen(f).read()
	soup = BeautifulSoup(myfile, "html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return text

def summarizeURL(url, total_pars):
	url_text = urlfetch(url).replace(u"Â", u"").replace(u"â", u"")

	fs = FrequencySummarizer()
	final_summary = fs.summarize(url_text.replace("\n"," "), total_pars)
	return " ".join(final_summary)

url = input("Enter a URL\n")
#textfromurl = urlfetch(url)
#print (textfromurl)
final_summary = summarizeURL(url, 5)
print (final_summary)