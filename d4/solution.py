import sys
#5-99 and 51-99

def fcontain( f_from, f_to, s_from, s_to):
    if f_from<=s_from and s_to<=f_to:
        return True
    if s_from<=f_from and f_to<=s_to:
        return True
    return False

def solution( lines):
    nf=0
    for line in lines:
        [first,second] = line.split(',')
        [f_from, f_to] = first.split('-')
        [s_from, s_to] = second.split('-')
        if fcontain( int(f_from), int(f_to), int(s_from), int(s_to)):
            #print(f'{first} and {second} is covered')
            nf+=1
        else:
            #print(f'{first} and {second} not covered')
            pass
    return nf

if __name__=='__main__':
    file1 = open(sys.argv[1] )
    lines = file1.readlines()
    file1.close()
    ans = solution(lines)
    print(f'{ans} pairs')
