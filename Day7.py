def opcodefunc (permanent, j):
    t = permanent.copy()
    
    adder = 3
    pointer = 0
    inputs = j
    count = 0

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
        if count > 4:
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
            t[t[i+1]] = inputs[pointer]
            pointer = pointer + 1
            i = i+2
        elif op == 4:
            inputs = inputs[0:adder] + [get(t[i+1], m1)] + inputs[adder:]
            adder = adder + 2
            i=0
            t = permanent.copy()
            count = count + 1
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
    return (inputs[10])



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


def day7part1 ():
    final = []
    f = open('opcode7.txt', 'r')
    s = f.read()
    permanent = [ int(s) for s in s.split(',')]
    preinputs = perms([0,1,2,3,4])
    inputs=[]
    for i in preinputs:
        inputs.append(i[0:1] + [0] + i[1:])
    for j in inputs:
        final.append(opcodefunc(permanent, j))
    print(max(final))
    

day7part1()
