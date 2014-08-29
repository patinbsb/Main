'''
Created on 26 Aug 2014

@author: patinbsb
'''
segment_hours=360/12
segment_minutes=360/60

def findangle(h,m):
    print((h*segment_hours)-(m*segment_minutes))

findangle(6,30)