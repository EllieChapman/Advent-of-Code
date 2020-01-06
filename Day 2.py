def opcodefunc (t):
    i = 0
    while i <= len(t)-1:
        if int(t[i]) == 99:
            break
        elif int(t[i]) == 1:
            x = int(int(t[int(t[i+1])]) + int(t[int(t[i+2])]))
            p = int(t[i+3])
            t[p] = x
            i = i+4
        elif int(t[i]) == 2:
            x = int(int(t[int(t[i+1])]) * int(t[int(t[i+2])]))
            p = int(t[i+3])
            t[p] = x
            i = i+4
    return(t[0])


def part1 ():
    f = open('opcode.txt', 'r')
    s = f.read()
    t = s.split(',')
    t[1]=12
    t[2]=2
    x = opcodefunc(t)
    print(x)
    if x==4138658:
        print('hooray!')
    else: print('booo')


def part2():
    for k in range(0,99):
        for j in range(0,99):
            f = open('opcode.txt', 'r')
            s = f.read()
            a = s.split(',')
            a[1]=k
            a[2]=j
            if opcodefunc(a) == 19690720:
                print(100 * k + j)


part1()

part2()
