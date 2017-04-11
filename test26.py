





def fact(i):
    sum = 0
    if i==0 :
        sum =1
    else:
        sum = i * fact(i-1)
    return sum


for i in range(5):
    print '%d! = %d' % (i,fact(i))

