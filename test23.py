

from sys import stdout


for a in range(4):
    for b in range(2-a+1):
        stdout.write(' ')
    for c in range(2*a+1):
        stdout.write('*')
    print

for d in range(3):
    for e in  range(d+1):
        stdout.write(' ')
    for f in range(4-2*d+1):
        stdout.write('*')
    print

