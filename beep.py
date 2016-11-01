#!/usr/bin/env python3
from time import sleep
import sys, os
import subprocess

def beep(pitch, time):
    x = 0
    time /= 1000
    #print(time)
    pitch = float(pitch)
    while x < time:
        print('\a')
        sleep(1/pitch)
        x += 1/pitch

#sys.stdout = open('/dev/console', 'w')
class Music():
    def __init__(self, musicfile):
        self.music = open(musicfile, 'r').read().splitlines()
        for num, data in enumerate(self.music):
            self.music[num] = data.split()
            #for number, datum in enumerate(self.music[num]):
                #self.music[num][number] = float(datum)
    def play(self):
        for data in self.music:
            #beep(data[0], data[1])
            beep(float(data[0]), float(data[1]))
            if len(data) == 3 and data[2]:
                #print(data[2])
                sleep(float(data[2])/1000)
    def beepplay(self):
        shargs = ['beep']
        for data in self.music:
            #shargs.__add__([' -f', data[0], ' -l', data[1]])
            shargs += [' -f', data[0], ' -l', data[1]]
            
            if len(data) == 3 and data[2]:
                shargs += [' -D', data[2]]
            shargs += [' -n']
        # why doesnt this work
        #subprocess.Popen(shargs)
        os.system(''.join(shargs))
        

#Music('mariooverkill.pymusic').play()
Music(sys.argv[1]).beepplay()
