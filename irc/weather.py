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
import tkMessageBox
from Tkconstants import LEFT
import Tkconstants
flag=0
api_key="AIzaSyAtbMGItIKXmcIEDv5_lPrtCWgVJ7PCovg"

'''
Grabbing the City and country geoip lookup from whatismyip.com
'''
def grabinfo(cityoveride,countryoveride,overide):
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
        edit("Google map could not find the information you entered, please try again\n")
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
        


    edit("Local weather for {0} in local area ({1},{2}) is...".format(strftime("%a, %d %b %Y %H:%M:%S", localtime()),city,country))
    edit ("Sky condition is {0}, {1}".format(status,descrip))
    edit("Temperature is {0} with highs of {1}".format(temp,temphigh))
    edit ("wind speed is {0} with rainfall in the past 3 hours of {1}".format(wind,rain))
    try:
        edit ("Gathered from the station of {0}".format(region))
    except:
        pass
    
    edit("If local area is inaccurate please enter your city name ")
def ending():
    global flag, newcity, newcountry
    flag=0
    edit ("Gathering new information...")
    edit ("")
    grabinfo(newcity,newcountry,1)
'''
defines the gui along with the button logic
'''
top=t.Tk()
def start():
    edit("Starting program, please wait")
    grabinfo("a","b",0)
def edit(input):
    output.config(state="normal")
    output.insert("insert",input+"\n")
    output.see(t.END)
    output.config(state="disabled")
def cityinput_but():
    cityinput(None)
def cityinput(e):
    global flag, newcity
    if flag==1:
        countryinput()
        return
    newcity=textinput.get()
    textinput.delete(0, t.END)
    edit("Please enter your country name ")
    edit("")
    flag=1
def countryinput():
    
    
    global newcountry
    newcountry=textinput.get()
    textinput.delete(0, t.END)
    ending()
button1=t.Button(top,text="start",command=start)

textinput=t.Entry(top,bd=5)
label=t.Label(top, text="City/country Entry")

scrollbar=t.Scrollbar()

output=t.Text(yscrollcommand=scrollbar.set)
output["yscrollcommand"]=scrollbar.set
button2=t.Button(top,text="Enter",command=cityinput_but)
edit("Please click start")
textinput.bind("<Return>",cityinput)
label.pack()
textinput.pack()
button2.pack()
scrollbar.pack(side=t.RIGHT, fill="y")
output.pack()
scrollbar.config(command=output.yview)
button1.pack()
top.mainloop()
