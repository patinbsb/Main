'''
Created on 26 Aug 2014

@author: patinbsb
'''

import socket
import string
import threading
from time import sleep
import Tkinter as t
from Tkinter import *
import json
import urllib

class Socket(object):
    def __init__(self,channel):
        HOST_EVENT=["199.9.251.213","199.9.252.26"]#second entry seems to be the one
        HOST="irc.twitch.tv" ##This is the Twitch IRC ip, don't change it.
        PORT=6667 ##Same with this port, leave it be.
        NICK="patinbsb" ##This has to be your bots username.
        self.NICK=NICK
        PASS="oauth:1ze7vvb6u80268qjot0uj1yk59ozq3u" ##Instead of a password, use this http://twitchapps.com/tmi/, since Twitch is soon updating to it.
        IDENT="patinbsb" ##Bot username again
        REALNAME="patinbsb" ##This doesn't really matter.
        CHANNEL="#"+channel ##This is the channel your bot will be working on.
        self.CHANNEL=CHANNEL
        self.s = socket.socket( ) ##Creating the socket variable
        s=self.s
        if CHANNEL=="#riotgames":
            s.connect((HOST_EVENT[1],PORT))
        else:
             s.connect((HOST, PORT)) ##Connecting to Twitch
        s.send("PASS %s\r\n" % PASS) ##Notice how I'm sending the password BEFORE the username!
        ##Just sending the rest of the data now.
        s.send("NICK %s\r\n" % NICK)
        s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
        ##Connecting to the channel.
        s.send("JOIN %s\r\n" % CHANNEL)
    


def threaded_loop(s,CHANNEL):
    readbuffer=""
    
    while (1):
            ##Receiving data from IRC and spitting it into manageable lines.
            readbuffer=readbuffer+s.recv(1024)
            #print readbuffer
            temp=string.split(readbuffer, "\n")
            readbuffer=temp.pop()
            for line in temp:
                chat_line=(line[line.find("#")+len(CHANNEL)+2:])
                chat_name=line[1:line.find("!")]
                chat_total=(chat_name+": "+chat_line)
                #print (chat_total)
                line=string.rstrip(line)
                line=string.split(line)    
                if(line[0]=="PING"):
                    s.send("PONG %s\r\n" % line[1])
                try:
                    new_gui.edit(chat_total)
                except:
                    pass
                sleep(0.1)


class Gui(object):
    
    
    def getviewers(self):
        viewer_raw=urllib.urlopen("https://api.twitch.tv/kraken/streams/{0}".format(self.CHANNEL[1:])).read()
        viewer_json=json.loads(viewer_raw)
        try:
            return (viewer_json["stream"]["viewers"])
        except:
            return ("N/A")
    
    def __init__(self,CHANNEL):
        self.CHANNEL=CHANNEL
        self.top=t.Tk()
        viewer_label=Label(self.top, text="{0} stream , Twitch Viewer count: {1}".format(self.CHANNEL[1:],str(self.getviewers())))
        self.text_input=Entry(self.top)
        self.scrollbar=Scrollbar()
        self.irc_feed=Text(yscrollcommand=self.scrollbar.set)
        viewer_label.pack()
    

    def irc_send(self,e):
        user_input=self.text_input.get()
        if "/join" in user_input:
            self.CHANNEL=user_input[user_input.find("/join")+5:]
            newsocket.s.send("JOIN %s\r\n" % self.CHANNEL)
            self.text_input.delete(0, END)
            viewer_input()
        else:
            newsocket.s.send(":{0}!{0}@{0}.tmi.twitch.tv ".format(newsocket.NICK)+"PRIVMSG "+self.CHANNEL+" :"+user_input+"\n")
            self.edit("patinbsb: "+user_input)
            self.text_input.delete(0, END)
    
   
    def viewer_input():
        viewer_label.config(text="{0} stream , Twitch Viewer count: {1}".format(self.CHANNEL[1:],str(self.getviewers())))
        top.after(30000,viewer_input)

    def edit(self,input):
        self.irc_feed.config(state="normal")
        self.irc_feed.insert("insert", input+"\n")
        self.irc_feed.insert("insert","\n")
        self.irc_feed.see(END)
        self.irc_feed.config(state="disabled")

    def main(self):
        
        self.scrollbar.pack(side=RIGHT, fill="y")
        self.irc_feed.pack(fill=BOTH, expand=1)
        self.text_input.pack(fill=BOTH, expand=1)
        self.scrollbar.config(command=self.irc_feed.yview)
        self.text_input.bind("<Return>",lambda event:self.irc_send(self))
        self.top.mainloop()
    
def main(channel):
    def threaded_loop(s,CHANNEL):
        readbuffer=""
        
        while (1):
                ##Receiving data from IRC and spitting it into manageable lines.
                readbuffer=readbuffer+s.recv(1024)
                #print readbuffer
                temp=string.split(readbuffer, "\n")
                readbuffer=temp.pop()
                for line in temp:
                    chat_line=(line[line.find("#")+len(CHANNEL)+2:])
                    chat_name=line[1:line.find("!")]
                    chat_total=(chat_name+": "+chat_line)
                    #print (chat_total)
                    line=string.rstrip(line)
                    line=string.split(line)    
                    if(line[0]=="PING"):
                        s.send("PONG %s\r\n" % line[1])
                    try:
                        new_gui.edit(chat_total)
                    except:
                        pass
                    sleep(0.1)
    newsocket=Socket(channel)
    newthread=threading.Thread(target=threaded_loop,args=(newsocket.s,newsocket.CHANNEL))               
    newthread.start()
    new_gui=Gui(newsocket.CHANNEL)
    new_gui.main()

if __name__=="__main__":
    main("wingsofdeath")
'''
    newsocket=Socket("wingsofdeath")
    newthread=threading.Thread(target=threaded_loop,args=(newsocket.s,newsocket.CHANNEL))               
    newthread.start()
    
    new_gui=Gui(newsocket.CHANNEL)
    new_gui.main()
'''




