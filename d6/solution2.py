import sys

def ismarker( s):
    return len(set(s))==4

def issom(s):
    return len(set(s))==14

def solution( line):
    for i in range(len(line)-4):
        pars = line[i:i+14]
        if issom(pars):
            return i+14
    return -1
file1 = open(sys.argv[1] )
lines = file1.readlines()
file1.close()
ans = solution(lines[0])
print(ans)
