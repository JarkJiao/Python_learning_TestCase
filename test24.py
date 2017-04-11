

#-*— coding:utf-8 -*-


#第一种办法
a = 2.0
b = 1.0
s = 0
for i in range(1,21):
    s += a/b
    t = a
    a = a+b
    b = t
print s


#第二种办法
l = []
for i in range(1,21):
    b,a = a,a+b
    l.append(a/b)

print reduce(lambda x,y:x+y,l)