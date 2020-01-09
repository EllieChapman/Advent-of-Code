def inserter(l, t):

    return [ l[0:i] + [t] + l[i:] for i in range(0, len(l)+1) ]

    #x = []
    #for i in range(0, len(l)+1):
        #a = l[0:i] + [t] + l[i:]
        #x.append(a)
    #return x

def perms(l):

    if len(l) == 0:
        return [[]]
    else:
        head = l[0]
        tail = l[1:]

        return [ x for sublist in perms(tail)
                   for x in inserter(sublist, head) ]
        
        #res = []
        #for sublist in perms(tail):
        #    j = inserter(sublist, head)
        #    res = res + j
        #return res

    
