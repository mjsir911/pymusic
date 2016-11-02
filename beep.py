#!/usr/bin/env python3
from time import sleep
import sys, os
import subprocess
from fcntl import ioctl
import sh2py

KIOCSOUND = int(19247)
reset     = -2
beeped    = 0

try:
    fd = open('/dev/console', 'wb')
except PermissionError:
    print('Not run as root, beeping to current session')
    cur_tty = os.ttyname(sys.stdout.fileno())
    #print(cur_tty)
    fd = open(cur_tty, 'wb')

    try:
        ioctl(fd, KIOCSOUND, 0)
    except OSError:
        print("""
        If you are going to run this script in an SSH session, run it as root.
        Otherwise, run it as a user on the actual machine so the speaker can
        be accessed.
        """)
        sys.exit(1)


def beep(pitch, time):
    if not pitch or not time:
        ioctl(fd, KIOCSOUND, int(0))
        return reset

    try:
        #Magic number courtesy of beep.c
        ioctl(fd, KIOCSOUND, int(1193180/pitch))
        # http://www.johnath.com/beep/beep.c
        # hope this isnt copyright infringement
        sleep(time/1000)
        return beeped
    except KeyboardInterrupt:
        beep(0, 0)
        raise


class Music():
    def __init__(self, musicfile):
        musicstring = open(musicfile, 'r').read()
        #print(musicstring)
        if 'bash' in musicstring or 'beep' in musicstring:
            self.music = sh2py.replace(musicstring).splitlines()
        else:
            self.music = musicstring.splitlines()

        for num, data in enumerate(self.music):
            self.music[num] = data.split()

    def play(self):
        for data in self.music:
            beep(float(data[0]), float(data[1]))
            if len(data) == 3 and data[2]:
                sleep(float(data[2])/1000)
        beep(0, 0)
    """def beepplay(self):
        Depreciated. Uses compiled beep.c module. Replaced with self.play()."""
    """
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
        """
Music(sys.argv[1]).play()
