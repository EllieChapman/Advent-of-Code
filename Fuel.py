def Fuel ():
    f = open('modules.txt', 'r')
    s = f.read()
    t = s.split('\n')
  #  print(t)
    a = 0
    for i in t:
        a = a + (int(int(i)/3)-2)
    print(a)
