#自由落体


a = 100.0
b = a/2

for i in  range(2,11):
    a += 2*b
    b /= 2

print a
print b