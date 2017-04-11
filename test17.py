import string

s = raw_input('input:\n')


w = 0
d = 0
space = 0
other = 0

for c in s:
    if c.isalpha():
        w+=1
    elif c.isdigit():
        d+=1
    elif c.isspace():
        space +=1
    else :
        other += 1

print 'char:%d,number:%d,space:%d,other:%d' % (w,d,space,other)

