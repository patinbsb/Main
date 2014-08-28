'''
Created on 26 Aug 2014

@author: patinbsb
'''
import urllib
import json
latlonglkup=urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address=bristol&key=AIzaSyAtbMGItIKXmcIEDv5_lPrtCWgVJ7PCovg").read()
jdata=json.loads(latlonglkup)
print jdata
#try:
lat,lng=(jdata["results"][0]["geometry"]["location"]["lat"],jdata["results"][0]["geometry"]["location"]["lng"])
#except:
    #print("Google map could not find the information you entered, please try again\n")
print lat,lng
