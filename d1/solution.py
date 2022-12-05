import sys

file1 = open(sys.argv[1] )
elfcal=0
elvescal=[]
nelfs=0
hcal=0
lines = file1.readlines()
file1.close()

lines.append('')
for idx, line in enumerate(lines):
    line = line.strip()
    if len(line)==0:
        nelfs+=1
        elvescal.append(elfcal)
        if elfcal > hcal:
            hcal = elfcal
        elfcal=0
    else:
        cal = int(line)
        elfcal+=cal
#maxcal = max(elvescal)
elvescal.sort(reverse=True)
max3cal = elvescal[:3]
maxcal = max3cal[0]
print(f'nelfs={nelfs}, maxcal={maxcal}, max3calsum={sum(max3cal)}')

