def orbits():
    f=open('orbits.txt', 'r')
    p=f.readlines()
    d=[]
    for pair in p:
        d.append((pair).replace("\n", ""))

    pair=[]
    for s in d:
        pair.append([s[0:3], s[4:]])
    #pair is list of pairs of stuff, 1st orboed by second

    di = {'COM' : 0}
    while len(pair)>0:
        temp = []
        for i in pair:
            if i[0] in di:
                di[i[1]] = di[i[0]] + 1
            else:
                temp.append(i)
        pair = temp

    count = 0
    for key in di:
        count = count + di[key]
    print(count)

    

def orbits2():
    f=open('orbits.txt', 'r')
    p=f.readlines()
    d=[]
    for pair in p:
        d.append((pair).replace("\n", ""))

    pair=[]
    for s in d:
        pair.append([s[0:3], s[4:]])


    #key is planet, value is what it orbits, so 1 to 1
    odi = {}
    for i in pair:
        odi[i[1]] = i[0]


    def pathcount(n):
        if n == 'COM':
            return [n]
        else:
            n2 = odi[n]
            return pathcount(n2) + [n]

    y = pathcount('YOU')
    s = pathcount('SAN')

    for i in range(0, len(y)):
        if y[i] != s[i]:
            print((len(y)-1-i) + (len(s)-1-i))
            break

    
