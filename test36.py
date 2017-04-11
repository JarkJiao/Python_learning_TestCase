

lower = int(raw_input('min_input:'))
upper = int(raw_input('max_input:'))

for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if i %  j ==0:
                break
        else:
            print i

