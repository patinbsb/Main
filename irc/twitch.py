"""This script attempts to use the activity of the chat room of a video stream to gauge and log
the interesting events which occur"""

import socket
import string
import time
from time import localtime, strftime
import urllib
import json
import datetime

time.clock()
'''Setting up info for irc connection'''
# IRC connection data
HOST_EVENT = ["199.9.251.213", "199.9.252.26"]  # second entry seems to be the one
HOST = "irc.twitch.tv"  # This is the Twitch IRC ip, don't change it.
PORT = 6667  # Same with this port, leave it be.
NICK = "patinbsb"  # This has to be your bots username.
PASS = "<Enter Pass HERE>"  # Instead of a password, use this http://twitchapps.com/tmi/, since Twitch is soon updating to it.
IDENT = "patinbsb"  # Bot username again
REALNAME = "patinbsb"  # This doesn't really matter.
CHANNEL = "#riotgames"  # This is the channel your bot will be working on.

'''obtaining the number of viewers'''
viewer_raw = urllib.urlopen("https://api.twitch.tv/kraken/streams/{0}".format(CHANNEL[1:])).read()
viewer_json = json.loads(viewer_raw)
viewer = (viewer_json["stream"]["viewers"])

'''creating the socket to connect to the irc'''
s = socket.socket()  # Creating the socket variable
if CHANNEL == "#riotgames":
    s.connect((HOST_EVENT[1], PORT))
else:
    s.connect((HOST, PORT))  # Connecting to Twitch
s.send("PASS %s\r\n" % PASS)  # Notice how I'm sending the password BEFORE the username!
# Just sending the rest of the data now.
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
# Connecting to the channel.
s.send("JOIN %s\r\n" % CHANNEL)

'''processing the info received by the socket'''

readbuffer = ""
# Eternal loop letting the bot run.
ticker = 0
combo = 0
oldtime = time.clock()
starttime = 0
endtime = 0
rate = 0
rate_starttime = 0
rate_endtime = 0
chat_capture = []
uptime = time.clock()
while (1):
    # Receiving data from IRC and spitting it into manageable lines.
    readbuffer = readbuffer + s.recv(1024)
    ticker += 1
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()
    for line in temp:
        chat_line = (line[line.find("#") + len(CHANNEL) + 2:])
        chat_name = line[1:line.find("!")]
        chat_total = (chat_name + ": " + chat_line)
        print (chat_total)
        line = string.rstrip(line)
        line = string.split(line)
        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])

    instant_rate = time.clock() - oldtime
    if ticker > 9 and rate_starttime == 0:
        rate_starttime = time.time()
    if ticker > 109 and rate_endtime == 0:
        rate_endtime = time.time()
        rate = ((rate_endtime - rate_starttime) / 100)
        for i in range(20):
            print ("**** TICKER CAPTURED ({0})****".format(str(rate)))


    #TODO: fix this so the instant_rate is relevant based on number of chat users
    if instant_rate < rate:
        if combo == 0:
            starttime = strftime("%a, %d %b %Y %H:%M:%S", localtime())
            starttime_file = strftime("%a, %d %b %Y %H,%M,%S", localtime())
        combo += 1
        chat_capture.append(chat_total)

    if instant_rate > rate:
        if combo > 20:
            endtime = strftime("%a, %d %b %Y %H:%M:%S", localtime())
            uptime_now = (time.clock() - uptime)
            tim = str(datetime.timedelta(seconds=uptime_now))
            form = tim.replace(":", "-")
            form2 = form.replace("-", "h ", 1)
            form3 = form2.replace("-", "m ")
            form4 = form3.replace(".", "s")
            with open(starttime_file + ", " + form4[:form4.find("s") + 1] + ".txt", "a") as f:
                f.write(starttime + " " + endtime + "\n")
                f.write("Seconds: " + str(float("{0:.2f}".format((time.clock() - uptime)))) + "\n")
                for line in chat_capture:
                    f.write(line + "\n")

            chat_capture = []
        combo = 0
    oldtime = time.clock()
