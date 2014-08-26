
##Socket library
import socket
import string
import time
from time import localtime, strftime
time.clock() 
##IRC connection data
HOST="irc.twitch.tv" ##This is the Twitch IRC ip, don't change it.
PORT=6667 ##Same with this port, leave it be.
NICK="patinbsb" ##This has to be your bots username.
PASS="oauth:1ze7vvb6u80268qjot0uj1yk59ozq3u" ##Instead of a password, use this http://twitchapps.com/tmi/, since Twitch is soon updating to it.
IDENT="patinbsb" ##Bot username again
REALNAME="patinbsb" ##This doesn't really matter.
CHANNEL="#tsm_theoddone" ##This is the channel your bot will be working on.
 
s = socket.socket( ) ##Creating the socket variable
s.connect((HOST, PORT)) ##Connecting to Twitch
s.send("PASS %s\r\n" % PASS) ##Notice how I'm sending the password BEFORE the username!
##Just sending the rest of the data now.
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
##Connecting to the channel.
s.send("JOIN %s\r\n" % CHANNEL)
 
readbuffer = ""
##Eternal loop letting the bot run.
ticker=0
combo=0
oldtime=time.clock()
starttime=0
endtime=0
while (1):
        ##Receiving data from IRC and spitting it into manageable lines.
        readbuffer=readbuffer+s.recv(1024)
        ticker+=1
        temp=string.split(readbuffer, "\n")
        readbuffer=temp.pop( )
        for line in temp:
            print(line[line.find("#")+len(CHANNEL)+2:])
            line=string.rstrip(line)
            line=string.split(line)    
            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])
                
        rate=time.clock()-oldtime
        #print(rate)
        if rate<0.1:
            if combo==0:
                starttime=strftime("%a, %d %b %Y %H:%M:%S", localtime())
            combo+=1
        if rate>0.2:
            if combo>5:
                endtime=strftime("%a, %d %b %Y %H:%M:%S", localtime())
                print(starttime,endtime)
            combo=0
        oldtime=time.clock()