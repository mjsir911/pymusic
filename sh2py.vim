" For translating copy-paste beep commands online to music file
:%s/beep//g
:%s/-n/
:%s/-f//g
:%s/^ *//g
:%s/-l//g
:%s/  / /g
:%s/-D//g
:%s/ $//g
:%s/^ *//g