import sys

tbl={ 'X':'A', 'Y':'B', 'Z':'C'}
score={ 'A': 1, 'B': 2, 'C': 3 }
vstbl = [ ('A', 'C'), ('B', 'A'), ('C', 'B')]
wintbl = {}  #peer to me
losetbl = {} #peer to me

for [m,p] in vstbl:
    losetbl[m] = p
    wintbl[p] = m

def compute_score( peer, strag):
    vssc = 0
    if strag=='X': # to lose
        me=losetbl[peer]
        vssc = 0
    elif strag=='Y': #to draw
        me = peer
        vssc = 3
    elif strag=='Z': #to win
        me = wintbl[peer]
        vssc = 6
    basesc = score[me]
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
    [peer, strag] = line.split(' ')
    sc = compute_score(peer, strag) 
    tsc += sc
print('total score=', tsc)
