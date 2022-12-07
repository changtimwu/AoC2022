import sys

def ismarker( s):
    return len(set(s))==4

def solution( line):
    for i in range(len(line)-4):
        pars = line[i:i+4]
        if ismarker(pars):
            return i+4
    return -1
file1 = open(sys.argv[1] )
lines = file1.readlines()
file1.close()
ans = solution(lines[0])
print(ans)
