from sys import stdout



for i in range(1,1000):
    k  = []
    n =-1
    s = i
    for j in range(1,i):
        if i % j == 0:
            n += 1
            s -= j
            k.append(j)

    if s == 0:
        print i
        for j in range(n):
            stdout.write(str(k[j]))
            stdout.write(' ')

        print k[n]
