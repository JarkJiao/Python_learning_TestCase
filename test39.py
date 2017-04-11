


if __name__ == '__main__':
    a = [1,10,22,32,42,53,63,73,83,91,100,0]  #  0很重要，谁用谁知道
    print 'the original list is :\n'
    for i in range(len(a)):
        print a[i]

    number = int(raw_input('input:\n'))

    end = a[10]
    if number  > end :
        a[11] = number
    else:
        for i in range(11):
            if a[i] > number:
                temp = a[i]
                a[i] = number
                for j in range(i+1,12):
                    temp1 = a[j]
                    a[j] = temp
                    temp = temp1
                break
    for i in range(len(a)):
        print a[i]
