

x = str(raw_input('input:\n'))

t = True

for i in range(len(x)/2):
    if x[i] != x[-1-i]:
        t = False
        break

if t:
    print 'yes!',x
else:
    print 'No!',x
