import sys
#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.

def getprio( ch):
    cval=ord(ch)
    if ch.islower():
        prio = cval - ord('a') + 1
    else:
        prio = cval - ord('A') + 27
    return prio

def split( line):
    l = int(len(line) /2)
    return line[:l], line[l:]

def find_common( s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    return list(s1.intersection(s2))

priosum=0
f = open( sys.argv[1], 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    if len(line)==0:
        continue
    (first,second) = split(line)
    cc = find_common(first,second)
    prio = getprio(cc[0])
    priosum+=prio
print('priosum=', priosum)
