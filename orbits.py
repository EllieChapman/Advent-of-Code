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


    di = {'COM': []}
    while len(pair)>0:
        temp = []
        for i in pair:
            if i[0] in di:
                di[i[0]].append(i[1])
                di[i[1]] = []
            else:
                temp.append(i)
        pair = temp

    #print(di)

    
    

    
