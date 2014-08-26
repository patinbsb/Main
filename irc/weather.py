'''
Created on 26 Aug 2014

@author: patinbsb
'''

import urllib
import urllib2
from bs4 import BeautifulSoup
import string
import re

response = urllib.urlopen('http://myexternalip.com/raw').read()
response2=urllib.urlopen('http://api.hostip.info/get_html.php?ip= %s &position=true'%response).read()
print(response2)
req=urllib2.Request("http://whatismyip.com",headers={'User-Agent' : "Magic Browser"})
response3=urllib2.urlopen(req).read()
soup=BeautifulSoup(response3)

city=soup.find("div",class_="the-city").get_text()
countryraw=soup.find("div",class_="the-country").get_text()

country=(re.sub(r'\W+', '', countryraw))
print (city,country)