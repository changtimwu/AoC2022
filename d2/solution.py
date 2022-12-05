import sys

tbl={ 'A':'X', 'B':'Y', 'C':'Z'}
score={ 'X': 1, 'Y': 2, 'Z': 3 }
wincases = [ ('X', 'Z'), ('Y', 'X'), ('Z', 'Y')]
def compute_score( peer, me):
    peer1 = tbl[peer] 
    basesc = score[me]
    vssc = 0
    if me == peer1:
        vssc=3
    elif (me, peer1) in wincases:
        vssc = 6
    return basesc + vssc


file1 = open(sys.argv[1] )
lines = file1.readlines()
file1.close()
tsc=0
lines.append('')
for idx, line in enumerate(lines):
    line = line.strip()
    if len(line)==0:
        continue
    [peer, me] = line.split(' ')
    sc = compute_score(peer, me) 
    tsc += sc
print('total score=', tsc)
