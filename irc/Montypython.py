"""
Created on 30 Aug 2014
Some unfinished test work/
@author: patinbsb
"""

import urllib

scenes = []
script = urllib.urlopen("http://www.sacred-texts.com/neu/mphg/mphg.htm").read()


class Scene(object):
    def __init__(self):
        pass

    def get_scene(self, n):
        scene_start = (script.find("<H4>Scene " + str(n)))
        scene_end = script[scene_start:].find("</PRE>")
        return script[scene_start + 23:(scene_end + scene_start)], scene_start, scene_end


c = Scene()
num = 1
while c.get_scene(num)[1] != -1 or c.get_scene(num)[2] != -1:
    scenes.append(c.get_scene(num)[0])
    print num
    if num == 11:
        num = 24
        continue
    num += 1
for i in scenes:
    print i