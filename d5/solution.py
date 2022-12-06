import sys


def parse_init_states( slines):
    poses =  list(range(1,36,4))
    #print(poses)
    hlists=[]
    for sline in slines:
        if len(sline)<36:
            sline += ' '* (36-len(sline))
        hlist = [sline[pos] for pos in poses]
        hlists.append(hlist)
    stacks = []
    #print('hlists=', hlists)
    for i in range(0,9):
        s=''
        for j in range(0,8):
            #print(f'stack[{i}][{j}]  <- hlists[{7-j}][{i}]={ hlists[7-j][i] }')
            s += hlists[7-j][i]
        stacks.append(s.strip())
    return stacks

def parse_moveline(line):
    toks = line.split(' ')
    return (int(toks[1]), int(toks[3]), int(toks[5]))

def loadlines( fn):
    file1 = open(fn )
    lines = file1.readlines()
    file1.close()

    bridx=-1
    for i, line in enumerate(lines):
        if len(line.strip())==0:
            bridx=i
            break
    initlines = lines[0:bridx]
    movelines = lines[bridx+1:]
    return initlines,movelines


initlines, movelines = loadlines( sys.argv[1])
stacks = parse_init_states( initlines)
print(stacks)

def move_between_stacks( ncrans, fromst, tost):
    for i in range(ncrans):
        origfrom = stacks[fromst-1]
        stacks[tost-1]+= origfrom[-1]
        stacks[fromst-1] = origfrom[:-1]

for line in movelines:
    (ncranes, fromst, tost) = parse_moveline(line)
    move_between_stacks( ncranes, fromst, tost)
print(stacks)

ans=''.join( [stack[-1] for stack in stacks if len(stack)>0])
print('ans=', ans)
