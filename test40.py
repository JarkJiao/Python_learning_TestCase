



if "__main__" == __name__:
    a = [1,2,3,4,5,6,7]
    print a

    for i in range(len(a)/2):
        a[i],a[len(a)-1-i] = a[len(a)-1-i],a[i]

    print a