def day8():
    f = open('day8.txt', 'r')
    s = f.read()

    zeros = 301
    count = 0
    layer = 51

    for i in range(0, 100):
        count = 0
        t = s[(150*i) : (150*(i+1))]
        for j in t:
            if j == '0':
                count = count + 1
        if count < zeros:
            zeros = count
            layer = i

    ones = 0
    twos = 0
    for i in s[(150*layer) : (150*(layer+1))]:
        if i == '2':
            twos = twos + 1
        elif i =='1':
            ones = ones + 1
    print(ones*twos)


def day8part2():
    f = open('day8.txt', 'r')
    s = f.read()

    l = ''

    for pixel in range(0, 150):
        for layer in range(0, 100):
            if s[(pixel+(150*layer))] == '1':
                l = l + 'w'
                break
            elif s[(pixel+(150*layer))] == '0':
                l = l + ' '
                break

    for i in range(0, 7):
        print(l[(i*25) : ((i*25)+25)])


day8()
day8part2()
