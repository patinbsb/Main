'''
Created on 26 Aug 2014

@author: patinbsb
'''
import json
dic={"hello":["n","i","g"]}
json.dump(dic, open("twitch.txt","w"))
'''
with open("twitch.txt","w") as f:
    for line in dic.values():
        f.write(line)

'''