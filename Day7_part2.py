def opcodefunc (permanent, j):

    codeA = permanent.copy()
    codeB = permanent.copy()
    codeC = permanent.copy()
    codeD = permanent.copy()
    codeE = permanent.copy()

    code = [codeA, codeB, codeC, codeD, codeE]
    eyes = [0,0,0,0,0]
    
    inputs = j
    holder = 0 #place to put outputs in and read inputs from
    switch = 1 #0 = take from holder, 1 take from phase
    counter = 0
    roundcount = 0
    def phase():
        return counter%5

    i = eyes[phase()]
    t = code[phase()]
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
            if roundcount < 5:
                if switch == 0:
                    t[t[i+1]] = holder
                    switch = 1
                    i = i + 2
                elif switch == 1:
                    t[t[i+1]] = inputs[phase()]
                    switch = 0
                    i = i+2
            elif roundcount >= 5:
                t[t[i+1]] = holder
                i = i + 2
        elif op == 4:
            holder = get(t[i+1], m1)
            eyes[phase()]=i+2
            counter = counter + 1
            roundcount = roundcount + 1
            i = eyes[phase()]
            t = code[phase()]
        elif op == 5:
            if get(t[i+1], m1) != 0:
                i = get(t[i+2], m2)
            else: i = i+3
        elif op == 6:
            if get(t[i+1], m1) == 0:
                i = get(t[i+2], m2)
            else: i = i+3
        elif op == 7:
            if get(t[i+1], m1) < get(t[i+2], m2):
                t[t[i+3]] = 1
            else: t[t[i+3]] = 0
            i = i + 4
        elif op == 8:
            if get(t[i+1], m1) == get(t[i+2], m2):
                t[t[i+3]] = 1
            else: t[t[i+3]] = 0
            i = i + 4
        else:
            print('unknown opcode', t[i])
            break
    return (holder)



def inserter(l, t):
    return [ l[0:i] + [t] + l[i:] for i in range(0, len(l)+1) ]

def perms(l):
    if len(l) == 0:
        return [[]]
    else:
        head = l[0]
        tail = l[1:]
        return [ x for sublist in perms(tail)
                   for x in inserter(sublist, head) ]


def day7part2():
    final = []
    f = open('opcode7.txt', 'r')
    s = f.read()
    permanent = [ int(s) for s in s.split(',')]
    inputs = perms([5,6,7,8,9])
    for j in inputs:
        final.append(opcodefunc(permanent, j))
    print(max(final))


day7part2()
