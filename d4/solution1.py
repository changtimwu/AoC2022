import sys

#2-4,6-8
def foverlap( b1, e1, b2, e2):
    return not (e1<b2 or e2<b1)

def solution( lines):
    nf=0
    for line in lines:
        [first,second] = line.split(',')
        [f_from, f_to] = first.split('-')
        [s_from, s_to] = second.split('-')
        if foverlap( int(f_from), int(f_to), int(s_from), int(s_to)):
            #print(f'{first} and {second} is overlap')
            nf+=1
    return nf

if __name__=='__main__':
    file1 = open(sys.argv[1] )
    lines = file1.readlines()
    file1.close()
    ans = solution(lines)
    print(f'{ans} pairs')
