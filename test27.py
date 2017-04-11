


def output(s,l):
    if l == 0:
        return
    print (s[l-1])
    output(s,l-1)

i = raw_input('input:')

l = len(i)

print output(i,l)