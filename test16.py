import datetime

if __name__ == '__main__':
    print (datetime.date.today().strftime('%Y-%m-%d'))

    jark = datetime.date(1994,4,8)

    print jark.strftime('%Y-%m-%d')

    jark1 = jark + datetime.timedelta(days=1)

    print jark1.strftime('%Y-%m-%d')

    jark2 = jark.replace(year=jark1.year + 1)

    print jark2.strftime('%Y-%m-%d')
