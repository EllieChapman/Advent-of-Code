def opcodefunc (t, theinput):
    i = 0
    def get(x, m):
        if m == 0:
            return t[x]
        if m == 1:
            return x
        print('unexpected mode',m)
        raise Exception
    while i <= len(t)-1:
        op = t[i]%100
        m1 = (t[i]//100)%10
        m2 = (t[i]//1000)%10
        if op == 99:
            break
        elif op == 1:
            x = get(t[i+1], m1) + get(t[i+2], m2)
            p = t[i+3]
            t[p] = x
            i = i+4
        elif op == 2:
            x = get(t[i+1], m1) * get(t[i+2], m2)
            p = t[i+3]
            t[p] = x
            i = i+4
        elif op == 3:
            t[t[i+1]] = theinput
            i = i+2
        elif op == 4:
            print(get(t[i+1], m1))
            i=i+2
        else:
            print('unknown opcode', t[i])
            break

def day2part1 ():
    f = open('opcode.txt', 'r')
    s = f.read()
    t = [ int(s) for s in s.split(',')]
    t[1]=12
    t[2]=2
    opcodefunc(t,999)
    x=t[0]
    print(x)
    if x==4138658:
        print('hooray!')
    else: print('booo')


def day5part1 ():
    f = open('day5input.txt', 'r')
    s = f.read()
    t = [ int(s) for s in s.split(',')]
    opcodefunc(t, 1)

day2part1()

day5part1()


