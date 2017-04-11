
i = int(raw_input('please input:\n'))

a = i/10000
b = i%10000/1000
c = i%1000/100
d = i%100/10
e = i%10


if a <>0:
    print 'five number:',e,d,c,b,a
elif b<>0:
    print 'four number:', e,d, c, b
elif c<>0:
    print 'three number:', e, d, c
elif d<>0:
    print 'two number:', e, d
else:
    print 'one number:',e
