'''
Created on 26 Aug 2014

uses ip geolocation to get current weather your your approximate location

@author: patinbsb
'''

import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import re
import time
from time import localtime,strftime
import Tkinter as t
top=t.Tk()
top.mainloop()
api_key="AIzaSyAwjprwMrCnyOvQqYEYfsGqKW2rPdrKtRg"
print("Loading Information... ")
print("")
'''
Grabbing the City and country geoip lookup from whatismyip.com
'''
def grabinfo(cityoveride,countryoveride,overide):

    response = urllib.urlopen('http://myexternalip.com/raw').read()
    req=urllib2.Request("http://whatismyip.com",headers={'User-Agent' : "Magic Browser"})
    response3=urllib2.urlopen(req).read()
    soup=BeautifulSoup(response3)
    city=soup.find("div",class_="the-city").get_text()
    countryraw=soup.find("div",class_="the-country").get_text()
    country=(re.sub(r'\W+', '', countryraw))
    ip=soup.find("div",class_="the-ip").get_text()
    
    if overide==1:
        city=cityoveride
        country=countryoveride
    '''
    using the google map api to get lat and lng informatin from city and country lookup
    '''
    latlonglkup=urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address= {0}+{1} &key= {2}".format(city,country,api_key)).read()
    jdata=json.loads(latlonglkup)
    try:
        lat,lng=(jdata["results"][0]["geometry"]["location"]["lat"],jdata["results"][0]["geometry"]["location"]["lng"])
    except:
        print("Google map could not find the information you entered, please try again")
        grabinfo("a","b",0)
    '''
    using openweathermap to get current weather information by lat and lng
    '''
    weather=urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}".format(lat,lng)).read()
    
    wdata=json.loads(weather)
    
    try:
        status=(wdata["weather"][0]["main"])
    except:
        status="unknown"
        pass
    try:    
        descrip=(wdata["weather"][0]["description"])
    except:
        descrip="unknown"
        pass
    try:    
        temp=(str(int(float(wdata["main"]["temp"])-273.15)))+" Degrees C"
    except:
        temp="unknown"
        pass
    try:    
        wind = (str(int(wdata["wind"]["speed"])*2.23))+" MPH"
    except:
        wind="unknown"
        pass
    try:    
        rain=(str(wdata["rain"]["3h"]))+" mm"
    except:
        rain="unknown"
        pass
    try:    
        temphigh=(str(int(float(wdata["main"]["temp_max"])-273.15)))+" Degrees C"
    except:
        temphigh="unknown"
        pass
    try:
        region=(wdata["name"])
    except:
        region="unknown"               
        


    print("Local weather for {0} in local area ({1}) is...".format(strftime("%a, %d %b %Y %H:%M:%S", localtime()),city))
    print ("Sky condition is {0}, {1}").format(status,descrip)
    print("Temperature is {0} with highs of {1}").format(temp,temphigh)
    print ("wind speed is {0} with rainfall in the past 3 hours of {1}".format(wind,rain))
    try:
        print ("Gathered from the station of {0}".format(region))
    except:
        pass
    newcity=raw_input("If local area is inaccurate please enter your city name ")
    newcountry=raw_input("Please enter your country name ")
    print ("Gathering new information...")
    print ("")
    grabinfo(newcity,newcountry,1)

grabinfo("a","b",0)
#print(status,descrip,temp,wind,rain,temphigh)
#print (city,country,ip)

