Tn = 0
Sn = []

n = int(raw_input('input1:\n'))

a = int(raw_input('input2:\n'))

for i in range(n):
    Tn += a
    a *=10
    Sn.append(Tn)
    print Tn

Sn =reduce(lambda x,y:x+y,Sn)

print Sn
